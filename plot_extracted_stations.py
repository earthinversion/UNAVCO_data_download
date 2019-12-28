import glob
import pandas as pd
from plotting_libs import plot_merc
import matplotlib.pyplot as plt
import numpy as np

def plot_extracted_stations(stations_df,plot_global=True):
    minlat, maxlat, minlon, maxlon = stations_df['Latitude'].min(),stations_df['Latitude'].max(),stations_df['Longitude'].min(),stations_df['Longitude'].max()
    if plot_global:
        map = plot_merc(resolution='h',llcrnrlon=-180, llcrnrlat=-85,urcrnrlon=180, urcrnrlat=85,topo=True)

    else:
        if np.abs(maxlat-minlat) < 10 and maxlat < 80 and minlat > -80:
            ddlat = 10
        elif maxlat < 89 and minlat > -89:
            ddlat = 1
        else:
            ddlat = 0

        if np.abs(maxlon-minlon) < 10 or np.abs(np.abs(maxlat-minlat)-np.abs(maxlon-minlon))<10 and maxlon < 170 and minlon > -170:
            ddlon = 10
        elif maxlon < 175 and minlon > -175:
            ddlon = 1
        else:
            ddlon = 0

        map = plot_merc(resolution='h',llcrnrlon=minlon-ddlon, llcrnrlat=minlat-ddlat,urcrnrlon=maxlon+ddlon, urcrnrlat=maxlat+ddlat,topo=True)

    for stalon,stalat in zip(stations_df['Longitude'],stations_df['Latitude']):
        x,y = map(stalon, stalat)
        map.plot(x, y,'^', color='b', markersize=7,markeredgecolor='k',linewidth=0.1)

    output = 'downloaded_stations_map.png'
    plt.savefig(output,dpi=300,bbox_inches='tight')
    print(f"Plot saved as {output}")
    plt.close('all')
