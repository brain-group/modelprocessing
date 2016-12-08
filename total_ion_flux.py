import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from general_functions import *
import matplotlib.lines as mlines
plt.style.use(['seaborn-talk', 'poster'])

df = pd.read_csv('Output/sphere_flux_batsrus_multi_fluid.csv')
df = df.sort_values('Unnamed: 0')
df_mfluid = df.set_index('Unnamed: 0')

df = pd.read_csv('Output/sphere_flux_batsrus_multi_species.csv')
df = df.sort_values('Unnamed: 0')
df_mspecies = df.set_index('Unnamed: 0')

dfs = {'fluid':df_mfluid, 'species':df_mspecies}
ls = {'fluid':'o-', 'species':'o--'}
color = {'H_p1':'DarkBlue', 'O2_p1':'DarkSlateBlue', 'O_p1':'Purple', 'CO2_p1':'MediumVioletRed'}


for dsk in ['fluid', 'species']:
    for ion in ['H_p1', 'O2_p1', 'O_p1', 'CO2_p1']:
        plt.plot(dfs[dsk][ion].index, dfs[dsk][ion].values, ls[dsk], color=color[ion],label=ion.replace('_', ''))

    if dsk == 'fluid':
        handles, labels = plt.gca().get_legend_handles_labels()

plt.xlabel('$\mathrm{Radius\;(R_M)}$')
plt.ylabel('$\mathrm{Total\;Ion\;Flux}$')
plt.semilogy()
leg1 = plt.legend(handles, labels, loc='upper left')
plt.gca().add_artist(leg1)

handles = []
for dsk in ['fluid', 'species']:
    line = mlines.Line2D([], [], color='k', ls=ls[dsk][1:], label=dsk)
    handles.append(line)

plt.legend(handles=handles, loc='upper right')


plt.savefig('Output/total_ion_flux.pdf')


