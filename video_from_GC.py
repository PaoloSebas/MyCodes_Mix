# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 10:10:06 2020

@author: Pablito
"""


import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import numpy as np
from celluloid import Camera
import ffmpeg

np.seterr(invalid='ignore'); # disable a warning from matplotlib + cartopy

access_cs_file1 = './GEOSChem.SpeciesConc.20171101_regional.nc4'
access_cs_file2 = './GEOSChem.SpeciesConc.20171201_regional.nc4'

access_cs_file3 = './GEOSChem.SpeciesConc.20180101_regional.nc4'
access_cs_file4 = './GEOSChem.SpeciesConc.20180201_regional.nc4'

access_cs_file5 = './GEOSChem.SpeciesConc.20180301_regional.nc4'


dset1 = xr.open_dataset(access_cs_file1)
dset2 = xr.open_dataset(access_cs_file2)

dset3 = xr.open_dataset(access_cs_file3)
dset4 = xr.open_dataset(access_cs_file4)
dset5 = xr.open_dataset(access_cs_file5)


j=0 # level


for i in range(0,30):
    
    clim1 = dset1['SpeciesConc_DMS'][i,j]
    
    fig = plt.figure(figsize=[24,10])
    
    east = 100
    west = 200
    north = -30
    south = -150
    # ax = fig.add_subplot(111, projection=ccrs.PlateCarree(central_longitude=0))
    
    # ax = plt.axes(projection=ccrs.AzimuthalEquidistant(central_latitude=-90, central_longitude=140.0))
    ax = plt.axes(projection=ccrs.SouthPolarStereo(central_longitude=0.0, true_scale_latitude=None, globe=None))
    
    ax.set_extent([west, east, south, north])
    ax.coastlines(resolution='110m')
    ax.gridlines()
    ax.set_title('Ciccio')
    
    clim1.plot.pcolormesh(ax=ax,
                       vmin=1e-10,
                       vmax=1e-9,
                       transform=ccrs.PlateCarree(),
                       cbar_kwargs={'label': clim1.units},
                       cmap='Greens'
                       )
    
    
    
    plt.show()

for i in range(0,31):
    
    clim2 = dset2['SpeciesConc_DMS'][i,j]
    
    east = 100
    west = 200
    north = -30
    south = -150
    
    fig = plt.figure(figsize=[24,10])
    
    
    # ax = fig.add_subplot(111, projection=ccrs.PlateCarree(central_longitude=0))
    
    # ax = plt.axes(projection=ccrs.AzimuthalEquidistant(central_latitude=-90, central_longitude=140.0))
    ax = plt.axes(projection=ccrs.SouthPolarStereo(central_longitude=0.0, true_scale_latitude=None, globe=None))
    
    ax.set_extent([west, east, south, north])
    ax.coastlines(resolution='110m')
    ax.gridlines()
    ax.set_title('Ciccio')
    
    clim2.plot.pcolormesh(ax=ax,
                        vmin=1e-10,
                        vmax=1e-9,
                        transform=ccrs.PlateCarree(),
                        cbar_kwargs={'label': clim2.units},
                        cmap='Greens'
                        )
    
    plt.show()

for i in range(0,31):
    
    clim3 = dset3['SpeciesConc_DMS'][i,j]
    
    east = 100
    west = 200
    north = -30
    south = -150
    
    fig = plt.figure(figsize=[24,10])
    
    
    # ax = fig.add_subplot(111, projection=ccrs.PlateCarree(central_longitude=0))
    
    # ax = plt.axes(projection=ccrs.AzimuthalEquidistant(central_latitude=-90, central_longitude=140.0))
    ax = plt.axes(projection=ccrs.SouthPolarStereo(central_longitude=0.0, true_scale_latitude=None, globe=None))
    
    ax.set_extent([west, east, south, north])
    ax.coastlines(resolution='110m')
    ax.gridlines()
    ax.set_title('Ciccio')
    
    clim3.plot.pcolormesh(ax=ax,
                        vmin=1e-10,
                        vmax=1e-9,
                        transform=ccrs.PlateCarree(),
                        cbar_kwargs={'label': clim3.units},
                        cmap='Greens'
                        )
    
    plt.show()

for i in range(0,28):
    
    clim4 = dset4['SpeciesConc_DMS'][i,j]
    
    east = 100
    west = 200
    north = -30
    south = -150
    
    fig = plt.figure(figsize=[24,10])
    
    
    # ax = fig.add_subplot(111, projection=ccrs.PlateCarree(central_longitude=0))
    
    # ax = plt.axes(projection=ccrs.AzimuthalEquidistant(central_latitude=-90, central_longitude=140.0))
    ax = plt.axes(projection=ccrs.SouthPolarStereo(central_longitude=0.0, true_scale_latitude=None, globe=None))
    
    ax.set_extent([west, east, south, north])
    ax.coastlines(resolution='110m')
    ax.gridlines()
    ax.set_title('Ciccio')
    
    clim4.plot.pcolormesh(ax=ax,
                        vmin=1e-10,
                        vmax=1e-9,
                        transform=ccrs.PlateCarree(),
                        cbar_kwargs={'label': clim4.units},
                        cmap='Greens'
                        )
    
    plt.show()

for i in range(0,31):
    
    clim5 = dset5['SpeciesConc_DMS'][i,j]
    
    east = 100
    west = 200
    north = -30
    south = -150
    
    fig = plt.figure(figsize=[24,10])
    
    
    # ax = fig.add_subplot(111, projection=ccrs.PlateCarree(central_longitude=0))
    
    # ax = plt.axes(projection=ccrs.AzimuthalEquidistant(central_latitude=-90, central_longitude=140.0))
    ax = plt.axes(projection=ccrs.SouthPolarStereo(central_longitude=0.0, true_scale_latitude=None, globe=None))
    
    ax.set_extent([west, east, south, north])
    ax.coastlines(resolution='110m')
    ax.gridlines()
    ax.set_title('Ciccio')
    
    clim5.plot.pcolormesh(ax=ax,
                        vmin=1e-10,
                        vmax=1e-9,
                        transform=ccrs.PlateCarree(),
                        cbar_kwargs={'label': clim5.units},
                        cmap='Greens'
                        )
    
    plt.show()
