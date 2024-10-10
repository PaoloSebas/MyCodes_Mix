import os
import xarray as xr
import matplotlib.pyplot as plt
import gcpy.plot as gcplot
from gcpy.plot.single_panel import single_panel

# wd = "mnt/d/PPO_Project_Sensitivity/Sensitivity\ /DATA_ANALYSIS/PPO_PROJECT"

wd = "/mnt/d/PPO/WORKING"

os.chdir(wd)

# Read data
ds = xr.open_dataset(
     "GEOSChem.SpeciesConc.20190101_0000z_wPPO.nc4"
)

print(ds.data_vars)

# Plot surface Ozone over the North Pacific

single_panel(

  ds['SpeciesConcVV_HO2'].isel(time=0,lev=0),
  title='HO2 conc',
  comap=plt.get_cmap("viridis"),
  log_color_scale=True,
  extent=[-180, 180, -90, 90]
)
plt.show()
