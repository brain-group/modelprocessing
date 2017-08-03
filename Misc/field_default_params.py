field_lims = {#'magnetic_field_x':(-50,50),
              #'magnetic_field_y':(-50,50),
              #'magnetic_field_z':(-50,50),
              'magnetic_field_x':(-20,30),
              'magnetic_field_y':(-10,40),
              'magnetic_field_z':(-20,20),
              'magnetic_field_total':(0,40),

              #'O_p1_number_density': (2e-4, 2e2),
              #'O2_p1_number_density':(1e-4, 30), 
              #'CO2_p1_number_density':(1e-4,1),
              'O2_p1_number_density':(1e-2,6e4),
              'O_p1_number_density': (4e0, 7e3),#(4e0, 2e4),
              'CO2_p1_number_density':(1e-2,6e3),

              #'H_p1_number_density': (1e-4, 1e3),#(4e0, 2e4),
              'H_p1_number_density':(7e-1,7e4),
              #'H_p1_number_density':(1e-1,1e2),
              'H_number_density':(1e-2, 1e5), 
              'He_number_density':(1e-2, 1e5),
              'electron_number_density':(1e-2, 1e5),
              #'magnetic_field_total':(0,120),
              'altitude':(5E1, 1e4),
              'magnetic_pressure':(0,0.3),
              'total_pressure':(0,0.5),
              'O2_p1_velocity_x':(-250,20),
              'O2_p1_velocity_y':(-50,150),
              'O2_p1_velocity_z':(-50,250),
              'O2_p1_velocity_total':(0,250),
              'O_p1_velocity_x':(-250,20),
              'O_p1_velocity_y':(-50,150),
              'O_p1_velocity_z':(-50,250),
              'O_p1_velocity_total':(0,325),
              'v_cross_B_total':(1e5, 1e9),
              'J_cross_B_total':(1e-6,5/1e2),
              }

field_lims_slices = {'O_p1_number_density': (1e-2, 5e4),
                     'O2_p1_number_density': (1e-2, 5e4),
                     'H_p1_number_density':(1e-3, 1e3),
                     'O_p1_temperature':(1e-3,1e2),
                     'pressure':(5e-3,4),
                     'magnetic_pressure':(5e-3, 30),
                     'O_p1_velocity_x':(-200,200),
                     'O_p1_velocity_y':(-200,200),
                     'O_p1_velocity_z':(-200,200),
                     'O2_p1_velocity_x':(-200,200),
                     'O2_p1_velocity_y':(-200,200),
                     'O2_p1_velocity_z':(-200,200),
                     'magnetic_field_x':(-30,30),
                     'magnetic_field_y':(-30,30),
                     'magnetic_field_z':(-10,10),
                     'magnetic_field_total':(1e-1,1e2), #(0,100),
                     'J_cross_B_total':(1e-3,5),
                     'J_cross_B_x':(-1,1),
                     'J_cross_B_y':(-5,5),
                     'J_cross_B_z':(-5,5),
                     'v_cross_B_total':(1e5, 1e9),
                     'O2_p1_v_cross_B_total':(1e-8, 1e-1),
                     'v_cross_B_x':(-5000,5000),
                     'v_cross_B_y':(-5000,5000),
                     'v_cross_B_z':(-5000,5000),
                     }
linthresh_slices = { 'v_cross_B_x':1,
                     'v_cross_B_y':1,
                     'v_cross_B_z':1,
                     'J_cross_B_x':1e-2,
                     'J_cross_B_y':1e-2,
                     'J_cross_B_z':1e-2,
                     }


field_lims_shells = {'O2_p1_flux':(-1e8, 1e8),
                     'O_p1_flux':(-4e7, 4e7),
                     'total_flux':(-1e8, 1e8),
                     'O_p1_number_density':(1e-7, 20),
                     'O2_p1_number_density':(1e-9, 50)}

log_fields2 = ['H_p1_number_density',
               'O2_p1_number_density',
               'O_p1_number_density',
               'CO2_p1_number_density',
               'altitude',
               'number_density',
               'current_total',
               'J_cross_B_total'
               ]
diverging_field_keys = ['flux']
symlog_field_keys = ['flux', 'velocity_normal','J_cross_B_x','J_cross_B_y','J_cross_B_z','v_cross_B_x']
log_field_keys = ['number_density', 'temperature', 'magnetic_pressure', 'pressure','current_total', 'J_cross_B_total',
                   'magnetic_field_total', 'v_cross_B_total']


vec_field_scale = {'magnetic_field':20,
                   'J_cross_B':100,
                   'v_cross_B':80}
