field_lims = {#'magnetic_field_x':(-50,50),
              #'magnetic_field_y':(-50,50),
              #'magnetic_field_z':(-50,50),
              'magnetic_field_x':(-20,30),
              'magnetic_field_y':(-10,40),
              'magnetic_field_z':(-20,20),
              'magnetic_field_total':(0,250),

              'H_p1_number_density': (0,2e4),#(1e-0, 1e2),#(4e0, 2e4),
              #'O_p1_number_density': (2e-4, 2e2),
              #'O2_p1_number_density':(1e-4, 30), 
              #'CO2_p1_number_density':(1e-4,1),
              'O2_p1_number_density':(1e-2,1e5),
              'O_p1_number_density': (1e-5, 2e3),#(4e0, 2e4),
              'CO2_p1_number_density':(1e-3,1e4),
              #'H_p1_number_density':(7e-1,7e4),

              'H_number_density':(1e-2, 1e5), 
              'He_number_density':(1e-2, 1e5),
              'electron_number_density':(1e-2, 1e5),
              #'magnetic_field_total':(0,120),
              'altitude':(5E1, 1e4),
              'magnetic_pressure':(0,0.3),
              'total_pressure':(0,1.5),
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
              'O2_p1_v_cross_B_x':(-0.002, 0.0002),
              'O2_p1_v_cross_B_y':(-0.002, 0.002),
              'O2_p1_v_cross_B_z':(-0.002, 0.002),
              'ram_pressure':(0,1),
              'J_cross_B_z':(-10,10),
              'H_p1_velocity_x':(-1000,10),
              'fluid_velocity_x':(-150,20),
              'H_p1_flux':(-1e-28,1e-28),
              'O_p1_flux':(-1e-28,1e-28),
              'O2_p1_flux':(-1e-28,1e-28),

              }

field_lims_slices = {'O_p1_number_density': (1e-1, 1e2),
                     'O2_p1_number_density': (1e-2, 5e1),
                     #'H_p1_number_density':(1e-4,1e-0),
                     'H_p1_number_density':(1e2, 1e4),
                     #'H_p1_number_density':(1e0, 1e2),
                     'O_p1_temperature':(1e-3,1e2),
                     'total_flux':(-1e8, 1e8),
                     'pressure':(5e-3,4),
                     'magnetic_pressure':(5e-3, 30),
                     'electron_velocity_total':(0,1000000),
                     'O_p1_velocity_x':(-400,400),
                     'O_p1_velocity_y':(-200,200),
                     'O_p1_velocity_z':(-200,200),
                     'O_p1_velocity_Esw':(-400,400),
                     'O_p1_velocity_Bperp':(-400,400),
                     'O_p1_velocity_normal':(-500,500),
                     'H_p1_velocity_x':(-400,400),
                     'H_p1_velocity_y':(-400,400),
                     'H_p1_velocity_z':(-400,400),
                     'H_p1_velocity_total':(200,600),
                     'O_p1_velocity_total':(1e0,600),
                     'O2_p1_velocity_x':(-400,400),
                     'O2_p1_velocity_Esw':(-400,400),
                     'O2_p1_velocity_Bperp':(-400,400),
                     'O2_p1_velocity_y':(-200,200),
                     'O2_p1_velocity_z':(-500,500),
                     'O2_p1_velocity_total':(1e0,500),
                     'magnetic_field_x':(-30,30),
                     'magnetic_field_y':(-30,30),
                     'magnetic_field_z':(-10,10),
                     'magnetic_field_total':(0,500),#(0,500), #(0,15),
                     'J_cross_B_total':(1e-3,5),
                     'J_cross_B_x':(-4,4),
                     'J_cross_B_y':(-4,4),
                     'J_cross_B_z':(-4,4),
                     'v_cross_B_total':(1e5, 1e9),
                     #'O2_p1_v_cross_B_total':(0,4e-3),#(1e-8, 1e-1),
                     'O2_p1_v_cross_B_total':(0,1e-1),#(1e-8, 1e-1),
                     'O2_p1_v_cross_B_total_normalized':(0,1e-6),#(1e-8, 1e-1),
                     'O2_p1_v_cross_B_z':(-3e-3, 3e-3),
                     'O2_p1_v_cross_B_x':(-3e-3, 3e-3),
                     'O_p1_v_cross_B_total':(0,4e-3),#(1e-8, 1e-1),
                     'O_p1_v_cross_B_z':(-3e-3, 3e-3),
                     'O_p1_v_cross_B_y':(-3e-3, 3e-3),
                     'O_p1_v_cross_B_x':(-3e-3, 3e-3),
                     'O_p1_v_cross_B_Esw':(-3e-3, 3e-3),
                     'O_p1_v_cross_B_normal':(-3e-3, 3e-3),
                     'O_p1_v_cross_B_Bperp':(-3e-3, 3e-3),
                     'O2_p1_v_cross_B_z':(-3e-3, 3e-3),
                     'O2_p1_v_cross_B_y':(-3e-3, 3e-3),
                     'O2_p1_v_cross_B_x':(-3e-3, 3e-3),
                     'O2_p1_v_cross_B_Esw':(-3e-3, 3e-3),
                     'O2_p1_v_cross_B_Bperp':(-3e-3, 3e-3),
                     'O2_p1_v_cross_B_normal':(-3e-3, 3e-3),
                     'v_cross_B_x':(-5000,5000),
                     'v_cross_B_y':(-5000,5000),
                     'v_cross_B_z':(-5000,5000),
                     'O2_p1_v_-_fluid_v_total':(0,300),
                     'O2_p1_v_-_fluid_v_x':(-300,300),
                     'O2_p1_v_-_fluid_v_y':(-300,300),
                     'O2_p1_v_-_fluid_v_z':(-300,300),
                     'O_p1_v_-_fluid_v_total':(0,300),
                     'O_p1_v_-_fluid_v_x':(-300,300),
                     'O_p1_v_-_fluid_v_y':(-300,300),
                     'O_p1_v_-_fluid_v_z':(-300,300),
                     'fluid_velocity_x':(-200,200),
                     'fluid_velocity_y':(-200,200),
                     'fluid_velocity_z':(-200,200),
                     'O2_p1_flux':(-1e8,1e8),
                     'O_p1_flux':(-1e9,1e9),
                     'O_p1_gyroradius':(0,20),
                     'O2_p1_gyroradius':(0,50),
                     "O_p1_flux_normalized":(-1e-18,1e-18),
                     "O2_p1_flux_normalized":(-1e-18,1e-18),
                     "O2_p1_v_cross_B_x_normalized":(-1e-6,1e-6),
                     "O2_p1_v_cross_B_Esw_normalized":(-1e-6,1e-6),
                     "O2_p1_v_cross_B_Bperp_normalized":(-1e-6,1e-6),
                     "O2_p1_v_cross_B_normal_normalized":(-1e-6,1e-6),
                     "magnetic_field_total_normalized":(0,2),
                     "O2_p1_gyroradius":(1e-1,1e3),
                     }
linthresh_slices = { 'v_cross_B_x':1,
                     'v_cross_B_y':1,
                     'v_cross_B_z':1,
                     'J_cross_B_x':1e-2,
                     'J_cross_B_y':1e-2,
                     'J_cross_B_z':1e-2,
                     'O2_p1_v_cross_B_z':1e-4,
                     'O2_p1_v_cross_B_x':1e-4,
                     'O_p1_v_cross_B_z':1e-4,
                     'O2_p1_velocity_z':1e-2,
                     'O2_p1_number_density_weighted_O2_p1_v_cross_B_z':\
                            1e-16,
                     'H_p1_flux_total':1e24,
                     'O_p1_flux_total':1e24,
                     'O2_p1_flux_total':1e24,
                     'O2_p1_velocity_x':1e-0,
                     'O2_p1_velocity_Esw':1e-0,
                     'O2_p1_velocity_Bperp':1e-0,
                     'O_p1_velocity_x':1e-0,
                     'O_p1_velocity_Esw':1e-0,
                     'O_p1_velocity_Bperp':1e-0,
                     'O_p1_velocity_normal':1e-0,
                     "O_p1_flux_normalized":1e-24,
                     "O2_p1_flux_normalized":1e-24,
                     }


field_lims_shells = {'O2_p1_flux':(-1e9, 1e9),
                     'O_p1_flux':(-1e8, 1e8),
                     'total_flux':(-1e8, 1e8),
                     'O_p1_number_density':(1e-7, 20),
                     'O2_p1_number_density':(1e-9, 50),
                     'magnetic_field_x':(-150,150),
                     'magnetic_field_y':(-150,150),
                     'magnetic_field_z':(-150,150),
                     'magnetic_field_normal':(-150,150),
                     'magnetic_field_total':(1e-1,300), 
                     'O_p1_v_cross_B_z':(-0.001,0.001),
                     'O_p1_velocity_normal':(-500,500),
                     'O2_p1_velocity_normal':(-500,500),
                     "O2_p1_gyroradius":(1e-1,1e3),
                     }

log_fields2 = [#'H_p1_number_density',
               'O2_p1_number_density',
               'O_p1_number_density',
               'CO2_p1_number_density',
               'altitude',
               'number_density',
               'current_total',
               'J_cross_B_total',
               ]
diverging_field_keys = ['flux', 'J_cross_B_y','magnetic_field_x', 'magnetic_field_y', 'magnetic_field_z', 'magnetic_field_normal', 'O_p1_v_cross_B_z', 'O2_p1_v_cross_B_z', 'O2_p1_velocity_z', 'O2_p1_velocity_z', 'O_p1_velocity_normal', 'O2_p1_velocity_normal', 'magnetic_field_Bperp', 'magnetic_field_Esw', 'O2_p1_v_cross_B_Bperp', 'O2_p1_v_cross_B_Esw', "O2_p1_velocity_Bperp", "O2_p1_velocity_Esw", "H_p1_velocity_Bperp", "H_p1_velocity_Esw", "H_p1_velocity_x", "O_p1_velocity_Esw", "O_p1_velocity_Bperp", "O_p1_v_cross_B_Bperp", "O_p1_v_cross_B_Esw", "O_p1_v_cross_B_normal", "O2_p1_v_cross_B_normal", "O2_p1_v_cross_B_x", "magnetic_field_orientation", 'magnetic_field_elevation_angle']
symlog_field_keys = ['flux', 'O2_p1_velocity_Esw', 'O2_p1_velocity_Bperp','O2_p1_velocity_x',  'O_p1_velocity_Esw', 'O_p1_velocity_Bperp','O_p1_velocity_x', "O_p1_velocity_normal", "O_p1_flux_normalized", "O2_p1_flux_normalized",]
log_field_keys = ['number_density', 'temperature', 'magnetic_pressure', 'pressure','current_total', 'J_cross_B_total',
               'O2_p1_velocity_total',"O_p1_velocity_total", "O2_p1_gyroradius", "O_p1_gyoradius"
                                         ]


vec_field_scale = {'magnetic_field':15,
                   'J_cross_B':100,
                   'v_cross_B':80,
                   'O2_p1_velocity':35}
