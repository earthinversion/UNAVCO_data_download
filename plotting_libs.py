from mpl_toolkits.basemap import Basemap,shiftgrid
import matplotlib.pyplot as plt
import numpy as np
import glob
import pandas as pd
import warnings, matplotlib.cbook
warnings.filterwarnings("ignore", category=FutureWarning)

DEG2KM = 111.2


def plot_topo(map,cmap=plt.cm.jet):
    #20 minute bathymetry/topography data
    etopo = np.loadtxt('topo/etopo20data.gz')
    lons  = np.loadtxt('topo/etopo20lons.gz')
    lats  = np.loadtxt('topo/etopo20lats.gz')
    # shift data so lons go from -180 to 180 instead of 20 to 380.
    etopo,lons = shiftgrid(180.,etopo,lons,start=False)
    lons, lats = np.meshgrid(lons, lats)
    # cs = map.contourf(lons,lats,etopo,30,cmap=plt.cm.jet,shading='interp')
    cs = map.pcolormesh(lons,lats,etopo,cmap=cmap,latlon=True,shading='gouraud')





def plot_merc(resolution,llcrnrlon,llcrnrlat,urcrnrlon,urcrnrlat,topo=True):
    warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)
    plt.figure(figsize=(8,8))
    map = Basemap(projection='merc',resolution = resolution, area_thresh = 1000., llcrnrlon=llcrnrlon, llcrnrlat=llcrnrlat,urcrnrlon=urcrnrlon, urcrnrlat=urcrnrlat)
    
    if topo:
        plot_topo(map,cmap=plt.cm.rainbow)

    map.drawcoastlines(color='k',linewidth=0.5)
    # map.fillcontinents()
    map.drawcountries(color='k',linewidth=0.1)
    map.drawstates(color='gray',linewidth=0.05)
    map.drawrivers(color='blue',linewidth=0.05)
    map.drawmapboundary()
    map.drawparallels(np.linspace(llcrnrlat,urcrnrlat,5,dtype='int16').tolist(),labels=[1,0,0,0],linewidth=0)
    map.drawmeridians(np.linspace(llcrnrlon,urcrnrlon,5,dtype='int16').tolist(),labels=[0,0,0,1],linewidth=0)
    return map

