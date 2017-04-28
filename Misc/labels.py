label_lookup = {'H_p1_number_density':r'$n(H+)$', #\;\mathrm{cm^{-3}}$',
          'O2_p1_number_density':u'$n(O_2+)$', #\;\mathrm{cm^{-3}}$',
          'O_p1_number_density':u'$n(O+)$', #\;\mathrm{cm^{-3}}$',
          'O_p2_number_density':u'$n(O++)$', #\;\mathrm{cm^{-3}}$',
          'CO2_p1_number_density':u'$n(CO_2+)$', #\;\mathrm{cm^{-3}}$',
          'H_number_density':u'$n(H)\;\mathrm{cm^{-3}}$',
          'He_number_density':u'$n(He)\;\mathrm{cm^{-3}}$',
          'electron_number_density':u'$n(e-)\;\mathrm{cm^{-3}}$',
          'number_density':u'$n\;\mathrm{cm^{-3}}$',
          'magnetic_field_radial':u'$B_r \mathrm{(nT)}$',
          'magnetic_field_x':u'$B_X \mathrm{(nT)}$',
          'magnetic_field_y':u'$B_Y \mathrm{(nT)}$',
          'magnetic_field_z':u'$B_Z \mathrm{(nT)}$',
          'magnetic_field_total':u'$|B| \mathrm{(nT)}$',
          'bats_min_LS270_SSL0':'BATSRUS: SSL=0',# (Solar min, LS=270)',
          'bats_min_LS270_SSL180':'BATSRUS: SSL=180',# (Solar min, LS=270)',
          'bats_min_LS270_SSL270':'BATSRUS: SSL=270',# (Solar min, LS=270)',
          'helio_1':'HELIOSARES: 1',# (Solar mod, LS=270)',
          'helio_2':'HELIOSARES: 2',# (Solar mod, LS=270)',
          'maven': "MAVEN",
          'maven2': "MAVEN-kp",
          'maven1': "MAVEN-sta",
          'altitude':'$\mathrm{Altitude}$',
          'magnetic_field_total':'$\mathrm{|B|\;(nT)}$',
          'number_density': '$\mathrm{n\;(cm^{-3})}$',
          'batsrus_multi_species':'BATSRUS Multi-Species',
          'batsrus_multi_fluid':'BATSRUS Multi-Fluid',
          'batsrus_electron_pressure':"BATSRUS Electron Pressure", 
          'heliosares':'HELIOSARES',
          'total_flux':'$\mathrm{Total\; Ion\;Flux}$',
          'x':'x', 'y':'y', 'z':'z',
          'CO2_p1_velocity_x':'$\mathrm{v_x(CO_2+)}$',
          'CO2_p1_velocity_y':'$\mathrm{v_y(CO_2+)}$',
          'CO2_p1_velocity_z':'$\mathrm{v_z(CO_2+)}$',
          'CO2_p1_velocity_xy':'$\mathrm{v_\perp(CO_2+)}$',
          'O_p1_velocity_x':'$\mathrm{v_x(O+)}$',
          'O_p1_velocity_y':'$\mathrm{v_y(O+)}$',
          'O_p1_velocity_z':'$\mathrm{v_z(O+)}$',
          'O_p1_velocity_xy':'$\mathrm{v_\perp(O+)}$',
          'O2_p1_velocity_x':'$\mathrm{v_x(O_2+)}$',
          'O2_p1_velocity_y':'$\mathrm{v_y(O_2+)}$',
          'O2_p1_velocity_z':'$\mathrm{v_z(O_2+)}$',
          'O2_p1_velocity_xy':'$\mathrm{v_\perp(O_2+)}$',
          'H_p1_velocity_x':'$\mathrm{v_x(H+)}$',
          'H_p1_velocity_y':'$\mathrm{v_y(H+)}$',
          'H_p1_velocity_z':'$\mathrm{v_z(H+)}$',
          'H_p1_velocity_xy':'$\mathrm{v_\perp(H+)}$',
          'electric_field_x':'$\mathrm{E_x}$',
          'electric_field_y':'$\mathrm{E_y}$',
          'electric_field_z':'$\mathrm{E_z}$',
          'electric_field_xy':'$\mathrm{E_\perp}$',
          'electron_pressure': '$P_e$',
          'magnetic_pressure': '$P_B$',
          'pressure':'$P$',
          'rhybrid':'Rhybrid',
          'rhybrid2':'Rhybrid',
          'rhcsv':'RHybrid-Analysator',
          'maven_plume':'maven',
          'maven_low_alt':'maven',
          }
label_lookup['H_p1_velocity_total'] = '$\mathrm{|v(H+)|}$'
label_lookup['H_p1_velocity_normal'] = '$\mathrm{v(H+)\cdot \hat{r}}$'
label_lookup['H_p1_flux'] = "$\mathrm{\Phi(H+)\;(\#/ (cm^{2} s) }$"
label_lookup['O2_p1_velocity_total'] = '$\mathrm{|v(O_2+)|}$'
label_lookup['O2_p1_velocity_normal'] = '$\mathrm{v(O_2+)\cdot \hat{r}\;(km/s)}$'
label_lookup['O2_p1_flux'] = "$\mathrm{\Phi(O_2+)\;(\#/ (cm^{2} s) }$"
label_lookup['CO2_p1_velocity_total'] = '$\mathrm{|v(CO_2+)|\;(km/s)}$'
label_lookup['CO2_p1_velocity_normal'] = '$\mathrm{v(CO_2+)\cdot \hat{r}\;(km/s)}$'
label_lookup['CO2_p1_flux'] = "$\mathrm{\Phi(CO_2+)\;(\#/ (cm^{2} s) }$"
label_lookup['O_p1_velocity_total'] = '$\mathrm{|v(O+)|}$'
label_lookup['O_p1_velocity_normal'] = '$\mathrm{v(O+)\cdot \hat{r}\;(km/s)}$'
label_lookup['O_p1_flux'] = "$\mathrm{\Phi(O+)\;(\#/ (cm^{2} s) }$"
label_lookup['area'] = '$\mathrm{dA}\;(cm^{2})$'
label_lookup['velocity_total'] = '$\mathrm{|v|\;(km/s)}$'
label_lookup['velocity_normal'] = '$\mathrm{v\cdot \hat{r}\;(km/s)}$'

for i in range(550, 660, 10):label_lookup['t00{0}'.format(i)] = 't00{0}'.format(i)
