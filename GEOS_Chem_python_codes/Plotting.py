#IMPORT necessary Libraries

import xarray as xr
import matplotlib.pyplot as plt
import netCDF4
import numpy as np
import gcpy.plot as gcplot
from gcpy.plot.single_panel import single_panel
from gcpy.plot.compare_single_level import compare_single_level
from gcpy.plot.compare_zonal_mean import compare_zonal_mean
from matplotlib.backends.backend_pdf import PdfPages

# Read data from PPO and NOPPO nc4 files

#COMPLETE DATASET

ds_i = xr.open_dataset(
    '/mnt/d/PPO/WORKING/MONTHLY/For the article/August2019_merged_ME_GEOSChem.SpeciesConc.20190801_0000z.nc4'
)

print('This is dataset_initial:', ds_i)
print('####################################################################################')


ds_f = xr.open_dataset(
    '/mnt/d/PPO/WORKING/MONTHLY/For the article/August2019_DIFF_30303_new_GEOSChem.SpeciesConc.20190801_0000z.nc4'
)

print('This is dataset_final', ds_f)
print('####################################################################################')

Species_X='HO2'
Species_X_units = 'SpeciesConcVV_HO2'
X = ds_i.variables[Species_X_units]
print(X)

print('########################## SUBSETTING ON Species:', Species_X, ': ##################################')
Xds_i = ds_i['SpeciesConcVV_HO2']
Xds_f = ds_f['SpeciesConcVV_HO2']

print('```````````````````````````````````````````````````````````````````')
print('This is the initial dataset after SUBSETTING on HO2', Xds_i)
print('```````````````````````````````````````````````````````````````````')

print('```````````````````````````````````````````````````````````````````')
print('This is the final dataset after SUBSETTING on HO2', Xds_f)
print('```````````````````````````````````````````````````````````````````')


# SUM over time and lev
Xi_sum = Xds_i.sum(dim=['time','lev'], keep_attrs=True)
Xf_sum = Xds_f.sum(dim=['time','lev'], keep_attrs=True)

# SUM only over time
Xdsi_time = Xds_i.sum(dim=['time'], keep_attrs=True)/31
Xdsi_time_ppb = Xdsi_time*1e+9
Xdsi_burden = np.sum(Xds_i.values)
Xdsf_time = Xds_f.sum(dim=['time'], keep_attrs=True)/31
Xdsf_time_ppb = Xdsf_time*1e+9
Xdsf_burden = np.sum(Xds_f.values)
Burden_var = ((Xdsf_burden - Xdsi_burden)/(Xdsi_burden))*100

print('Burden i:', Xdsi_burden)
print('Burden f:', Xdsf_burden)
print('% Variation:', Burden_var)

#print(f"Sum (molmol-1 dry) of Xdsi_time: {np.sum(Xdsi_time.values)}")
#print(f"Sum (molmol-1 dry)of Xdsf_time: {np.sum(Xdsf_time.values)}")
#print(f"Sum (ppb) of Xdsi_time: {np.sum(Xdsi_time.values)*1e+9}")
#print(f"Sum (ppb) of Xdsf_time: {np.sum(Xdsf_time.values)*1e+9}")

#diff_time = ((Xdsf_time - Xdsi_time)/(Xdsi_time))*100
diff_plot = ((Xdsf_time_ppb - Xdsi_time_ppb)/(Xdsi_time_ppb))*100
max_diff_plot = np.max(diff_plot.values)
min_diff_plot = np.min(diff_plot.values)

print('Maximum value in diff_plot:',max_diff_plot)
print('Minimum value in diff_plot:',min_diff_plot)

def max_modulus(a, b):
    if abs(a) > abs(b):
        return a
    else:
        return b

max_plot = max_modulus(max_diff_plot,min_diff_plot)
print('max_plot:', max_plot)

#print(f"Sum  of diff_time on all values: {np.sum(diff_time.values)}")

abs_max=abs(max_plot)
print('The scale max value in the plot is:',abs_max,'%')


single_panel(
  diff_plot.isel(lev=51),
  title=Species_X + ' % change- August 2019 - LEV=51',
  comap=plt.get_cmap("bwr"),
  log_color_scale=False,
    #vmin= -abs_max,
    #vmax= abs_max,
     vmin= -15,
     vmax= 15,
   extent=[-180, 180, -90, 90]
)

plt.show()

