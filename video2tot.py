# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 11:17:47 2020

@author: Pablito
"""


import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import numpy as np
from celluloid import Camera
import ffmpeg


access_cs_file1 = './GEOSChem.SpeciesConc.20180201_0000z.nc4'
dset1 = xr.open_dataset(access_cs_file1)

j=0 # level

for i in range(0,30):
    
    clim1 = dset1['SpeciesConc_SO2'][i,j]
    
    fig = plt.figure(figsize=[24,10])
    
  
    ax = fig.add_subplot(111, projection=ccrs.PlateCarree(central_longitude=0))
    
    # # ax = plt.axes(projection=ccrs.AzimuthalEquidistant(central_latitude=-90, central_longitude=140.0))
    # ax = plt.axes(projection=ccrs.SouthPolarStereo(central_longitude=0.0, true_scale_latitude=None, globe=None))
    ax.coastlines(resolution='110m')
    ax.gridlines()
    ax.set_title('Ciccio')
    
    clim1.plot.pcolormesh(ax=ax,
                       # vmin=1e-10,
                       # vmax=1e-9,
                       transform=ccrs.PlateCarree(),
                       cbar_kwargs={'label': clim1.units},
                       cmap='Reds'
                       )
    
    
    
    plt.show()
