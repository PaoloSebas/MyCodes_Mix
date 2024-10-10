import xarray as xr
import matplotlib.pyplot as plt
from gcpy.plot.compare_single_level import compare_single_level
from gcpy.plot.compare_zonal_mean import compare_zonal_mean

# Read data
gcc_ds = xr.open_dataset(
    '/mnt/d/PPO/WORKING/MONTHLY/For the article/August2019_merged_ME_GEOSChem.SpeciesConc.20190801_0000z.nc4'
)
modified_ds = xr.open_dataset(
    '/mnt/d/PPO/WORKING/MONTHLY/For the article/August2019_DIFF_30303_new_GEOSChem.SpeciesConc.20190801_0000z.nc4'
)

# Plot comparison of surface ozone over the North Pacific
compare_single_level(
    gcc_ds,
    'GEOS-Chem with PPO tail',
    modified_ds,
    'Without all PPO contribution',
    varlist=['SpeciesConcVV_HO2'],
    extra_title_txt='Surface'
)
plt.show()
