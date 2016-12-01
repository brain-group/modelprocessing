import numpy as np
import matplotlib.pyplot as plt
import h5py
from general_functions import *
import sys
import getopt
plt.style.use('seaborn-talk')

def setup_plot(fields, ds_names, coords, tlimit=None, add_altitude=False):
    if add_altitude: 
        fields = fields[:]
        fields.insert(0,'altitude')
    Nfields = len(fields)
        
    hrs = [1 for i in range(Nfields+1)]
        
    hrs.insert(0,0.1)
    hrs.insert(0,0.1)
    import matplotlib.gridspec as gridspec
    gs = gridspec.GridSpec(Nfields+2, 1,
                           height_ratios=hrs, hspace=0.05)
    axes = [plt.subplot(gs[i, 0]) for i in range(2, Nfields+2)]
    f = plt.gcf()
    
    #f, axes = plt.subplots(len(fields), 1)
    colors = {'maven':'k', 
              'bats_min_LS270_SSL0':'CornflowerBlue',
              'bats_min_LS270_SSL180':'DodgerBlue',
              'bats_min_LS270_SSL270':'LightSkyBlue',
              'batsrus_multi_species':'MediumBlue',
              'batsrus_multi_fluid':'DodgerBlue',
              'heliosares':'MediumVioletRed',
              'helio_1':'LimeGreen',
              'helio_2':'ForestGreen'}
    
    plot = {}
    plot['axes'] = {field:ax for field, ax in zip(fields, axes)}
    plot['kwargs'] = {ds:{ 'label':label_lookup[ds], 'color':colors[ds], 'lw':1.5}
                        for ds in ds_names}
    plot['kwargs']['maven']['alpha'] = 0.6
    plot['kwargs']['maven']['lw'] = 1
    plot['figure'] = f
    plot['ax_arr'] = axes
    plot['N_axes'] = Nfields #len(fields)
    plot['shadowbar'] = plt.subplot(gs[0,0])
    plot['timebar'] = plt.subplot(gs[1,0])
    plot['tlimit'] = tlimit
    plot['shadow'] = np.logical_and(coords[0]<0,
                                    np.sqrt(coords[1]**2+coords[2]**2)<3390)
    return plot

def finalize_plot(plot, xlim=None, fname=None, show=False, zeroline=False):
    if 'altitude' in plot.keys():
        plot['axes']['altitude'].plot(np.linspace(plot['time'][0], plot['time'][-1],
                                                  plot['altitude'].shape[0]), 
                                                  plot['altitude'],
                                                                                                                          **plot['kwargs']['maven'])
    for f, ax in plot['axes'].items():
        ax.set_ylabel(label_lookup[f])
        ax.set_xlim(plot['time'][0], plot['time'][-1])
        if zeroline:
            ax.hlines(0, ax.get_xlim()[0], ax.get_xlim()[1], linestyle=':', alpha=0.4)
        if f in field_lims: ax.set_ylim(field_lims[f])
        if f in log_fields2: ax.set_yscale('log')
            
    for i in range(plot['N_axes']):
        ax = plot['ax_arr'][i]
        if i == plot['N_axes']-1: ax.set_xlabel('$\mathrm{Time}$')
        else: ax.set_xticks([])
        
        if plot['tlimit'] is not None:
            lim, t = plot['tlimit'], plot['time']
            tlim = (t[int(lim[0]*t.shape[0])], t[int(lim[1]*t.shape[0])])
            ax.set_xlim(tlim)
            
    tb = plot['timebar']
    sb = plot['shadowbar']
    
    t_xv, t_yv = np.meshgrid(np.linspace(0,1, plot['time'].shape[0]), [0,1])
    s_xv, s_yv = np.meshgrid(np.linspace(0, 1, plot['shadow'].shape[0]),[0,1])
                             
    t_dat = np.array([plot['time'], plot['time']])
    s_dat = np.array([plot['shadow'], plot['shadow']])
    
    tb.pcolormesh(t_xv, t_yv, t_dat, cmap='inferno',rasterized=True)
    sb.pcolormesh(s_xv, s_yv, s_dat, cmap='inferno_r',rasterized=True,
                  vmin=-0.1,vmax=1.2)
    
    if plot['tlimit'] is None: tlim = (0,1)
    else: tlim = plot['tlimit']
    
    tb.set_xlim(tlim)
    sb.set_xlim(tlim)
    
    tb.axis('off')
    sb.axis('off')
    
    
    

    
    #plot['ax_arr'][-1].legend()#(bbox_to_anchor=(1.4, 1))
    handles, labels = plot['ax_arr'][-1].get_legend_handles_labels()
    plot['ax_arr'][0].legend(handles, labels)
    plot['ax_arr'][0].set_zorder(1)
    plot['figure'].set_size_inches(8,10)
    if show:
        plt.show()
    if fname is None:
        plt.savefig('Output/test.pdf')
    else:
        plt.savefig(fname)

def get_path_idxs(coords, ds_names, ds_types):
    indxs = {}
    for ds_type, keys in ds_types.items():
        if ds_type == 'maven': continue
        if len(keys) == 0: continue
        print 'getting indxs: '+ds_type
        indxs[ds_type] = bin_coords(coords, ds_names[keys[0]], 
                                    grid=ds_type=='heliosares')
    indxs['maven'] = 'all'
    return indxs

def plot_field_ds(x, data, ax, kwargs):
    if data.ndim<2:
        ax.plot(x, data, **kwargs)
    else:
        mean_dat = np.nanmedian(data,axis=0)
        max1_dat = np.nanpercentile(data, 75, axis=0)
        min1_dat = np.nanpercentile(data, 25, axis=0)
        max0_dat = np.nanmax(data, axis=0)
        min0_dat = np.nanmin(data, axis=0)
        ax.plot(x, mean_dat, **kwargs)
        
        ax.fill_between(x, min1_dat, max1_dat, alpha=0.2, color=kwargs['color'])
        lim = ax.get_ylim()
        ax.fill_between(x, min0_dat, max0_dat, alpha=0.05, color=kwargs['color'])
        ax.set_ylim(lim)


def make_plot(times, fields, orbits, title, indxs, coords, ds_names, ds_types, skip=1, subtitle=None, tlimit=None):
    plot = setup_plot(fields, ds_names.keys(), coords,
                      tlimit=tlimit, add_altitude=True)

    for ds_type, keys in ds_types.items():
        for key in keys:
            dsf = ds_names[key]

            for field in fields:
                with h5py.File(dsf, 'r') as ds:
                    ds_dat = get_ds_data(ds, field, indxs[ds_type],
                                         grid=ds_type=='heliosares')
                        
                    if ds_dat.size != 0:
			plot_field_ds(times-times[0], ds_dat, plot['axes'][field], plot['kwargs'][key])
		    else:
			plot_field_ds(np.array([0]),np.array([0]),
                                      plot['axes'][field], plot['kwargs'][key])
    import pandas as pd
    data = pd.read_csv('Output/test_orbit.csv',
            names=['mso_x','mso_y', 'mso_z', 'alt', 'O2_p1_number_density',
                   'O_p1_number_density', 'CO2_p1_number_density',
                   'H_p1_number_density', 'electron_number_density',
                   'magnetic_field_x', 'magnetic_field_y',
                   'magnetic_field_z'])
    data['magnetic_field_total'] = np.sqrt(data['magnetic_field_x']**2+
                                           data['magnetic_field_y']**2+
                                           data['magnetic_field_z']**2)
    for field in fields:
	dsf = ds_names['maven'] 
	mav_data = []

	#for i, orb in enumerate(orbits):
       #     if np.sum(dat.shape) != 0: mav_data.append(dat[field])     

	#if len(mav_data) == 0: 
	#    plot_field_ds(np.array([0]), np.array([0]), plot['axes'][field], plot['kwargs']['maven'])
	#    continue

	#L = min([d.shape[0] for d in mav_data])
	#data = np.zeros((len(mav_data),L))
	#for i in range(len(mav_data)):
	#    data[i] = mav_data[i][:L]
	#t = np.linspace(times[0], times[-1], data.shape[1])-times[0]
	t = np.linspace(times[0], times[-1], data.shape[0])-times[0]
	#plot_field_ds(t[::skip], data[:,::skip], plot['axes'][field], plot['kwargs']['maven'])
        print t.shape, data.shape
	plot_field_ds(t[::skip], 1.5*data[field][::skip], plot['axes'][field], 
                      plot['kwargs']['maven'])
    plot['altitude'] = data['alt']
    plot['time'] = t
    if subtitle is None: subtitle= orbits[0]
    print 'Saving: ', 'Output/{0}_{1}.pdf'.format(title, subtitle)
    finalize_plot(plot, zeroline=True, fname='Output/{0}_{1}.pdf'.format(title, subtitle))
    


def flythrough_orbit(orbits, ds_names, ds_types, field, **kwargs):

    #coords, times = get_path_pts(trange, Npts=150)
    coords = get_path_pts_adj(orbits[0])[:, ::10]
    times = np.linspace(0,1,coords.shape[1])
    indxs = get_path_idxs(coords, ds_names, ds_types)

    if field == 'ion':
        fields =['H_p1_number_density',
                'O2_p1_number_density',
                'O_p1_number_density',
                'CO2_p1_number_density'] 
        tlimit = (0.3, 0.7)
        title = 'ion_flythrough'
        skip = 1
    elif field == 'mag':
        fields = ['magnetic_field_total', 'magnetic_field_x', 'magnetic_field_y',
              'magnetic_field_z']
        tlimit = (0.3, 0.7)
        title = 'mag_flythrough'
        skip = 1

    make_plot(times, fields, orbits, title, indxs, coords,
              ds_names, ds_types, tlimit=tlimit, skip=skip, **kwargs)


def main(argv):

    try:
        opts, args = getopt.getopt(argv,"f:o:n:",["field=", "orbit=", "new_models"])
    except getopt.GetoptError:
        print 'error'
        return


    field, orbit, new_models = None, None, False

    for opt, arg in opts:
        if opt in ("-f", "--field"):
            field = arg
        elif opt in ("-o", "--orbit"):
            orbit = int(arg)
        elif opt in ("-n", "-new_models"):
            print 'Using new models'
            new_models=True

    if orbit == 371:
        orbit_groups = np.array([353, 360, 363, 364, 364, 365, 366, 367, 367, 368, 369, 370, 371,375, 376, 376, 380, 381, 381, 382, 386, 386, 387, 390, 391])
    
    # Get Datasets setup
    ds_names, ds_types = get_datasets(new_models=new_models)

        #tranges = get_orbit_times(orbits)
        #mid_tr = tranges[:, orbits.shape[0]/2]
    flythrough_orbit([orbit], ds_names, ds_types, field)


if __name__ == "__main__":
    main(sys.argv[1:])
