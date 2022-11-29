# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 20:46:33 2020

@author: Pablito
"""

    
import sys
import os 
import matplotlib
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd
from datetime import datetime
import glob
import cartopy.crs as ccrs
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import matplotlib.gridspec as gridspec
from mpl_toolkits.axes_grid1 import make_axes_locatable



# Variables Initialization 

#int

choosen_x = 0
choosen_y = 0
choosen_z = 0 

#strings

yes = ''
no = ''
# units_x=''
# units_t=''
hhmm=''
units_conv_x=''

#arrays
X1 = []
Y1 = []
Z1 = []

X2 = []
Y2 = []
Z2 = []

X3 = []
Y3 = []
Z3 = []

X4 = []
Y4 = []
Z4 = []

header_frame = []

#########FUNCTIONS


##### ADDING COLORBAR

def add_colorbar(data_inp, cax_inp, units_z_inp):
    
    colorbar=fig.colorbar(data_inp, cax=cax_inp)
    colorbar.set_label(content_z+ ' (' +units_z_inp+')', rotation=270, labelpad=10)
    colorbar.ax.tick_params(labelsize=font_size)
    

######## COUNTING FILES ###########

txtCounter_v1 = len(glob.glob1('./v1', "*.txt"))
txtCounter_v2 = len(glob.glob1('./v2', "*.txt"))
txtCounter_v3 = len(glob.glob1('./v3', "*.txt"))
txtCounter_v4 = len(glob.glob1('./v4', "*.txt"))


print(txtCounter_v1)
print(txtCounter_v2)
print(txtCounter_v3)
print(txtCounter_v4)


#########LISTING TXT FILES organized in four directories ################# 


txt_files_list_v1 = glob.glob("./v1/*.txt")
txt_files_list_v1 = sorted(txt_files_list_v1)

txt_files_list_v2 = glob.glob("./v2/*.txt")
txt_files_list_v2 = sorted(txt_files_list_v2)

txt_files_list_v3 = glob.glob("./v3/*.txt")
txt_files_list_v3 = sorted(txt_files_list_v3)

txt_files_list_v4 = glob.glob("./v4/*.txt")
txt_files_list_v4 = sorted(txt_files_list_v4)


fname_dictionary_v1 = {}
fname_dictionary_v2 = {}
fname_dictionary_v3 = {}
fname_dictionary_v4 = {}


#########DICTIONARies OF FILE NAMES################# 

for number in range(0,txtCounter_v1):
      fname_dictionary_v1["fnamev1_%s" %number] = txt_files_list_v1[number]

print(fname_dictionary_v1)

for number in range(0,txtCounter_v2):
      fname_dictionary_v2["fnamev2_%s" %number] = txt_files_list_v2[number]

print(fname_dictionary_v2)

for number in range(0,txtCounter_v3):
      fname_dictionary_v3["fnamev3_%s" %number] = txt_files_list_v3[number]

print(fname_dictionary_v3)

for number in range(0,txtCounter_v4):
      fname_dictionary_v4["fnamev4_%s" %number] = txt_files_list_v4[number]

print(fname_dictionary_v4)

#########STORING THE HEADER################# 

# Reading the header with genfromtxt, specified the str format
read_header = np.genfromtxt(fname_dictionary_v1["fnamev1_0"], dtype = str)

# Creating the frame with pandas for the header

header_frame = pd.DataFrame(data=read_header[0])
print(header_frame)

################# STORING THE REST OF THE FILES FOR EACH voyage (v) #######

txt_frame_tot_v1 = pd.DataFrame()
txt_frame_tot_v2 = pd.DataFrame()
txt_frame_tot_v3 = pd.DataFrame()
txt_frame_tot_v4 = pd.DataFrame()

###### V1 ###############

for number in range(0,txtCounter_v1):
    
    read_txt_v1 = np.genfromtxt(fname_dictionary_v1["fnamev1_%s" %number], skip_header=1)
    # print('primo passo')
    # print(read_txt)
    
    txt_frame_v1 = pd.DataFrame(data=read_txt_v1)
    # print(txt_frame)
    # print('secondo passo')

    txt_frame_tot_v1 = txt_frame_tot_v1.append(txt_frame_v1, ignore_index=True)
    # print('dentro')
    # print(txt_frame_tot)

#print('fuori loop')
print(txt_frame_tot_v1)

# Until this point I have stored two frames: header and the rest of 
# Data Block (They are header_frame and txt_frame_tot)
    

## STORING THE NUMBER OF LINES for txt_frame_tot
    
index_v1 = txt_frame_tot_v1.index
number_of_rows_v1 = len(index_v1)
print(number_of_rows_v1)

###### V2 ###############

for number in range(0,txtCounter_v2):
    
    read_txt_v2 = np.genfromtxt(fname_dictionary_v2["fnamev2_%s" %number], skip_header=1)
    # print('primo passo')
    # print(read_txt)
    
    txt_frame_v2 = pd.DataFrame(data=read_txt_v2)
    # print(txt_frame)
    # print('secondo passo')

    txt_frame_tot_v2 = txt_frame_tot_v2.append(txt_frame_v2, ignore_index=True)
    # print('dentro')
    # print(txt_frame_tot)

#print('fuori loop')
print(txt_frame_tot_v2)

# Until this point I have stored two frames: header and the rest of 
# Data Block (They are header_frame and txt_frame_tot)
    
    ## STORING THE NUMBER OF LINES for txt_frame_tot
    
index_v2 = txt_frame_tot_v2.index
number_of_rows_v2 = len(index_v2)
print(number_of_rows_v2)


###### V3 ###############

for number in range(0,txtCounter_v3):
    
    read_txt_v3 = np.genfromtxt(fname_dictionary_v3["fnamev3_%s" %number], skip_header=1)
    # print('primo passo')
    # print(read_txt)
    
    txt_frame_v3 = pd.DataFrame(data=read_txt_v3)
    # print(txt_frame)
    # print('secondo passo')

    txt_frame_tot_v3 = txt_frame_tot_v3.append(txt_frame_v3, ignore_index=True)
    # print('dentro')
    # print(txt_frame_tot)

#print('fuori loop')
print(txt_frame_tot_v3)

# Until this point I have stored two frames: header and the rest of 
# Data Block (They are header_frame and txt_frame_tot)
    
    ## STORING THE NUMBER OF LINES for txt_frame_tot
    
index_v3 = txt_frame_tot_v3.index
number_of_rows_v3 = len(index_v3)
print(number_of_rows_v3)


###### V4 ###############

for number in range(0,txtCounter_v4):
    
    read_txt_v4 = np.genfromtxt(fname_dictionary_v4["fnamev4_%s" %number], skip_header=1)
    # print('primo passo')
    # print(read_txt)
    
    txt_frame_v4 = pd.DataFrame(data=read_txt_v4)
    # print(txt_frame)
    # print('secondo passo')

    txt_frame_tot_v4 = txt_frame_tot_v4.append(txt_frame_v4, ignore_index=True)
    # print('dentro')
    # print(txt_frame_tot)

#print('fuori loop')
print(txt_frame_tot_v4)
pinco = type(txt_frame_tot_v4)
print(pinco)

# Until this point I have stored two frames: header and the rest of 
# Data Block (They are header_frame and txt_frame_tot)
    
    ## STORING THE NUMBER OF LINES for txt_frame_tot
    
index_v4 = txt_frame_tot_v4.index
number_of_rows_v4 = len(index_v4)
print(number_of_rows_v4)

# ##### CONVERTING COLUMN 0 and 1(UTC) in DATETIME "Readable"
# ##### The DATEs are stored in txt_frame_tot_v(i)

for number in range(0,number_of_rows_v1):
    
     pivot = txt_frame_tot_v1.iloc[number,0]
   #  print('soy el primero', pivot)
     pivot = int(pivot)
   #  print('soy el segundo', pivot)
     pivot = str(pivot)
   #  print('soy el tercero', pivot)
    
     txt_frame_tot_v1.iloc[number,0] = datetime.strptime(pivot , "%Y%m%d")

for number in range(0,number_of_rows_v2):
    
     pivot2 = txt_frame_tot_v2.iloc[number,0]
   #  print('soy el primero', pivot)
     pivot2 = int(pivot)
   #  print('soy el segundo', pivot)
     pivot2 = str(pivot)
   #  print('soy el tercero', pivot)
    
     txt_frame_tot_v2.iloc[number,0] = datetime.strptime(pivot2 , "%Y%m%d")
    
for number in range(0,number_of_rows_v3):
    
     pivot3 = txt_frame_tot_v3.iloc[number,0]
   #  print('soy el primero', pivot)
     pivot3 = int(pivot)
   #  print('soy el segundo', pivot)
     pivot3 = str(pivot)
   #  print('soy el tercero', pivot)
    
     txt_frame_tot_v3.iloc[number,0] = datetime.strptime(pivot3 , "%Y%m%d")
    
for number in range(0,number_of_rows_v4):
    
     pivot4 = txt_frame_tot_v4.iloc[number,0]
   #  print('soy el primero', pivot)
     pivot4 = int(pivot)
   #  print('soy el segundo', pivot)
     pivot4 = str(pivot)
   #  print('soy el tercero', pivot)
    
     txt_frame_tot_v4.iloc[number,0] = datetime.strptime(pivot4 , "%Y%m%d")

print(txt_frame_tot_v1)
print(txt_frame_tot_v2)
print(txt_frame_tot_v3)
print(txt_frame_tot_v4)


# ###### PLOTTING  #######

# #Input the x and y you need

choosen_x = int(input('Choose the number (between 1 and 217) of the x-variable (for example 1 for UTC): '))
choosen_y = int(input('Choose the number (between 1 and 217) of the y-variable (for example 8 for TEMP): '))

print('Please choose a Z coordinate in case you want to create a colorbar or 3D plot.')

choosen_z = int(input('Choose the number (between 1 and 217) of the z-variable (for example 3 for LAT): '))

content_x = header_frame.iat[choosen_x,0]
content_y = header_frame.iat[choosen_y,0]
content_z = header_frame.iat[choosen_z,0]

print('X is:', content_x)
print ('Y is:', content_y)
print ('Z is:', content_z)

#Determining Units

units_x = (input('What are the Units for x?: '))    
units_y = (input('What are the Units for y?: '))
units_z = (input('What are the Units for z?: '))


### V1 ######

#Filling X1, Y1, Z1 arrays

for i in txt_frame_tot_v1:
    
    X1 = txt_frame_tot_v1.loc[0:number_of_rows_v1, choosen_x]

#print (X1)

for i in txt_frame_tot_v1:
    
    Y1 = txt_frame_tot_v1.loc[0:number_of_rows_v1, choosen_y]

for i in txt_frame_tot_v1:
    
    Z1  = txt_frame_tot_v1.loc[0:number_of_rows_v1, choosen_z]


### V2 ######
#Filling X2, Y2, Z2 arrays

for i in txt_frame_tot_v2:
    
    X2 = txt_frame_tot_v2.loc[0:number_of_rows_v2, choosen_x]

#print (X2)

for i in txt_frame_tot_v2:
    
    Y2 = txt_frame_tot_v2.loc[0:number_of_rows_v2, choosen_y]

for i in txt_frame_tot_v2:
    
    Z2  = txt_frame_tot_v2.loc[0:number_of_rows_v2, choosen_z]
    
### V3 ######
#Filling X3, Y3, Z3 arrays

for i in txt_frame_tot_v3:
    
    X3 = txt_frame_tot_v3.loc[0:number_of_rows_v3, choosen_x]

#print (X3)

for i in txt_frame_tot_v3:
    
    Y3 = txt_frame_tot_v3.loc[0:number_of_rows_v3, choosen_y]

for i in txt_frame_tot_v1:
    
    Z3  = txt_frame_tot_v3.loc[0:number_of_rows_v3, choosen_z]

### V4 ######
#Filling X4, Y4, Z4 arrays

for i in txt_frame_tot_v4:
    
    X4 = txt_frame_tot_v4.loc[0:number_of_rows_v4, choosen_x]

#print (X4)

for i in txt_frame_tot_v4:
    
    Y4 = txt_frame_tot_v4.loc[0:number_of_rows_v4, choosen_y]

for i in txt_frame_tot_v4:
    
    Z4  = txt_frame_tot_v4.loc[0:number_of_rows_v4, choosen_z]
    
    

print('What kind of plot do you want create?')
print('Your options are: 1: X-Y, 2:LON-LAT + Colorbar, 3: 3D ')

Plot_chosen = (input('Number:?'))

zdata_v1 = Z1
xdata_v1 = X1
ydata_v1 = Y1

zdata_v2 = Z2
xdata_v2 = X2
ydata_v2 = Y2
    
zdata_v3 = Z3
xdata_v3 = X3
ydata_v3 = Y3
    
zdata_v4 = Z4
xdata_v4 = X4
ydata_v4 = Y4

if Plot_chosen == '1':
    
    # 2D
    
    fig =plt.figure(figsize=(9,4))
    ax = plt.axes()
    ax.axis('auto')
    ax.set_xlabel(content_x+ ' (' +units_x+')')
    ax.set_ylabel(content_y+ ' (' +units_y+')')
    # ax.xticks(fontsize=5)
    # ax.yticks(fontsize=5)
    # ax.title(' ' +content_x+ ' vs ' +content_y)
    ax.scatter(X1,Y1)
    # plt.scatter(X2,Y2, s=1)
    # plt.scatter(X3,Y3, s=1)
    #plt.scatter(X4,Y4, s=1)

    
elif  Plot_chosen == '2':
    
    fig = plt.figure(figsize=(9,4))
    ax = fig.add_axes([0.1,0.1,0.7,1])
    
    colorbar_ax1 = fig.add_axes([0.9, 0.1, 0.02, 0.9])
    colorbar_ax2 = fig.add_axes([1.0, 0.1, 0.02, 0.9])
    colorbar_ax3 = fig.add_axes([1.1, 0.1, 0.02, 0.9])
    colorbar_ax4 = fig.add_axes([1.2, 0.1, 0.02, 0.9])
    
    # ########## WITH COLORBAR #############
        
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.coastlines('110m', linewidth=2)
    ax.set_extent([60, 180, -30, -90], ccrs.PlateCarree())
    ax.set_title('A.A. (v1-v4)', pad=30)
    
    # ax.set_xlabel(content_x+ ' (' +units_x+')')
    # ax.set_ylabel(content_y+ ' (' +units_y+')')
    # #ax.set_zlabel(content_z+ ' (' +units_z+')')
    
    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                        linewidth=0.8, color='gray', alpha=0.2, linestyle='--')
    
    # # gl.xlabels_top = False
    gl.ylabels_right = False
    gl.xlines = True
    #gl.xlocator = mticker.FixedLocator([-180, -45, 0, 45, 180])
    gl.xformatter = LONGITUDE_FORMATTER
    gl.yformatter = LATITUDE_FORMATTER
    gl.xlabel_style = {'color': 'black', 'size':10}
    gl.ylabel_style = {'color': 'black', 'size':10}
    
    cm_v1 = plt.cm.get_cmap('YlGn')
    cm_v2 = plt.cm.get_cmap('Reds')
    cm_v3 = plt.cm.get_cmap('Blues')
    cm_v4 = plt.cm.get_cmap('Oranges')
    
    ciccio_v1=ax.scatter(xdata_v1, ydata_v1, c=zdata_v1, cmap=cm_v1, s=1)
    ciccio_v2=ax.scatter(xdata_v2, ydata_v2, c=zdata_v2, cmap=cm_v2, s=1)
    ciccio_v3=ax.scatter(xdata_v3, ydata_v3, c=zdata_v3, cmap=cm_v3, s=1)
    ciccio_v4=ax.scatter(xdata_v4, ydata_v4, c=zdata_v4, cmap=cm_v4, s=1)
    
    # # ###  colorbar
    
    font_size = 10 # Adjust as appropriate.
    
    add_colorbar(ciccio_v1, colorbar_ax1, units_z)
    add_colorbar(ciccio_v2, colorbar_ax2, units_z)
    add_colorbar(ciccio_v3, colorbar_ax3, units_z)
    add_colorbar(ciccio_v4, colorbar_ax4, units_z)

elif  Plot_chosen == '3':
    
    print('Not available for now')

elif Plot_chosen == '4':
    
    east = 170
    west = 80
    north = -20
    south = -90
    
    X = []
    Y = []
    Z = []
    
    for i in range(0,number_of_rows_v1):
    
      
        
        XX = X1[i]
        YY = Y1[i]
        ZZ = Z1[i]

        fig=plt.figure(figsize=(18, 8), constrained_layout=True)
    
        ax = fig.add_axes([0.1,0.1,0.7,1])
    
    # colorbar_ax1 = fig.add_axes([0.9, 0.1, 0.02, 0.9])
    # colorbar_ax2 = fig.add_axes([1.0, 0.1, 0.02, 0.9])
    # colorbar_ax3 = fig.add_axes([1.1, 0.1, 0.02, 0.9])
    # colorbar_ax4 = fig.add_axes([1.2, 0.1, 0.02, 0.9])
    
    # fig = plt.figure(figsize=(15,4), constrained_layout=True)
    # spec_fig = fig.add_gridspec(ncols=2, nrows=1, width_ratios=[8,5], height_ratios=[1])
    
    # ax0 = fig.add_subplot(spec_fig[0, 0])
    # ax1 = fig.add_subplot(spec_fig[0, 1])
    # ax1.axis('off')
        
        ax = plt.axes(projection=ccrs.AzimuthalEquidistant(central_latitude=-90.0, central_longitude=140.0))
        ax.set_extent([west, east, south, north])

        ax.coastlines(resolution='110m')
        ax.set_title('A.A. 2017/2018 (v1-v4)', fontsize=30, pad=30)
    #ax.stock_img()
        ax.gridlines()
    
    
        ax.set_xlabel(content_x+ ' (' +units_x+')')
        ax.set_ylabel(content_y+ ' (' +units_y+')')
    #ax.set_zlabel(content_z+ ' (' +units_z+')')
    
        cm_v1 = plt.cm.get_cmap('YlGn')
    # cm_v2 = plt.cm.get_cmap('Reds')
    # cm_v3 = plt.cm.get_cmap('Blues')
    # cm_v4 = plt.cm.get_cmap('Oranges')
    
    
        
        ciccio_v1=ax.scatter(XX, YY, c=ZZ, cmap=cm_v1, transform=ccrs.Geodetic(), s=3)
    # ciccio_v2=ax.scatter(xdata_v2, ydata_v2, c=zdata_v2, cmap=cm_v2, transform=ccrs.Geodetic(), s=3)
    # ciccio_v3=ax.scatter(xdata_v3, ydata_v3, c=zdata_v3, cmap=cm_v3, transform=ccrs.Geodetic(), s=3)
    # ciccio_v4=ax.scatter(xdata_v4, ydata_v4, c=zdata_v4, cmap=cm_v4, transform=ccrs.Geodetic(), s=3)
    
    
        plot1= ciccio_v1
    # plot2= ciccio_v2
    # plot3= ciccio_v3
    # plot4= ciccio_v4
    
        font_size = 20 # Adjust as appropriate.
    
        v1 = 'Davis'
    # v2 = 'Casey'
    # v3 = 'Mawson & Davis'
    # v4 = 'Macquarie Island'

    

        colorbar1=fig.colorbar(ciccio_v1, cax=colorbar_ax1, fraction=0.3)
        colorbar1.set_label(content_z+ ' (' +units_z+')', rotation=270, labelpad=20, fontsize=20)
        colorbar1.ax.tick_params(labelsize=font_size)
    
    # colorbar2=fig.colorbar(ciccio_v2, cax=colorbar_ax2, fraction=0.3)
    # colorbar2.set_label(content_z+ ' (' +units_z+')', rotation=270, labelpad=20, fontsize=20)
    # colorbar2.ax.tick_params(labelsize=font_size)
    
    # colorbar3=fig.colorbar(ciccio_v3, cax=colorbar_ax3, fraction=0.3)
    # colorbar3.set_label(content_z+ ' (' +units_z+')', rotation=270, labelpad=20, fontsize=20)
    # colorbar3.ax.tick_params(labelsize=font_size)
    
    # colorbar4=fig.colorbar(ciccio_v4, cax=colorbar_ax4, fraction=0.3)
    # colorbar4.set_label(content_z+ ' (' +units_z+')', rotation=270, labelpad=20, fontsize=20)
    # colorbar4.ax.tick_params(labelsize=font_size)
    
  
        plt.scatter([], [], c='green', alpha=0.5, s=50,label=str(v1))
    # plt.scatter([], [], c='red', alpha=0.5, s=50,label=str(v2))
    # plt.scatter([], [], c='blue', alpha=0.5, s=50,label=str(v3))
    # plt.scatter([], [], c='orange', alpha=0.5, s=50,label=str(v4))

  
    plt.legend(scatterpoints=1, frameon=False,
           labelspacing=1, loc='lower left', fontsize=15);
    


    
   
    
    
    
   
