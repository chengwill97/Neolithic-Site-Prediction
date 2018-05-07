import os
import csv
import numpy  as np
import pandas as pd

import matplotlib

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


def plotPredictedFromDF(site_df, 
                        nonsite_df, 
                        model_name='prediction', 
                        country='Ireland',
                        resolution='c',
                        alpha_predicted=1.0,
                        s_predicted=1,
                        alpha_common=1.0,
                        s_common=2):
    """Plot points of Ireland
    
    Parameters
    -----------
        site_df : pandas.DataFrame
            dataframe of the sites

        nonsite_df : pandas.DataFrame
            dataframe of the nonsites

        model_name : str, optional
            name of the model to use

        country : str, optional
            name of the country to focus on

        resolution : str, optional
            resolution of boundary database to use. 
            Can be c (crude), l (low), i (intermediate), 
            h (high), f (full) or None. 

            If None, no boundary data will be read in 
            (and class methods such as drawcoastlines 
            will raise an if invoked). Resolution drops 
            off by roughly 80% between datasets. Higher 
            res datasets are much slower to draw.
            
    Returns
    --------
        None
    """
    country_df = site_df.where(site_df['country'] == country)
    nonsites_df = nonsite_df.where(nonsite_df[model_name] == 1)

    minlat = country_df['latitude'].min()
    maxlat = country_df['latitude'].max()
    minlon = country_df['longitude'].min()
    maxlon = country_df['longitude'].max()
    difflat = maxlat - minlat
    difflon = maxlon - minlon
    minlat -= (difflat / 10) * 2
    maxlat += (difflat / 10) * 2
    minlon -= (difflon / 10) * 2
    maxlon += (difflon / 10) * 2

    """
    Plot the geographical features,
    common sites coordinates, and
    predicted coordinates
    """
    projection='cyl'
    basemap = Basemap(projection=projection,
                llcrnrlat=minlat,
                urcrnrlat=maxlat,     
                llcrnrlon=minlon,
                urcrnrlon=maxlon,
                resolution=resolution)
    basemap.drawparallels(np.arange(int(minlat),int(maxlat),1),labels=[1,0,0,0])
    basemap.drawmeridians(np.arange(int(minlon),int(maxlon),1),labels=[0,0,0,1])
    basemap.drawcoastlines()
    basemap.drawcountries()
    basemap.drawstates()
    # basemap.fillcontinents(color='None')
    # basemap.drawrivers()
    # basemap.fillcontinents(color='#04BAE3', lake_color='#FFFFFF')
    # basemap.drawmapboundary(fill_color='#FFFFFF')

    # Plot predicted points
    predicted_sites = Basemap(projection=projection,
                        llcrnrlat=minlat,
                        urcrnrlat=maxlat,     
                        llcrnrlon=minlon,
                        urcrnrlon=maxlon,
                        resolution=resolution)
    lat = np.array(nonsites_df['latitude'].tolist())
    lon = np.array(nonsites_df['longitude'].tolist())
    x, y = predicted_sites(lon, lat)
    predicted_sites.scatter(x, y, c='b', marker='o', s=s_predicted, alpha=alpha_predicted)

    # Plot common site points 
    common_sites = Basemap(projection=projection,
                     llcrnrlat=minlat,
                     urcrnrlat=maxlat,     
                     llcrnrlon=minlon,
                     urcrnrlon=maxlon,
                     resolution=resolution)
    lat = np.array(country_df['latitude'].tolist())
    lon = np.array(country_df['longitude'].tolist())
    x, y = common_sites(lon, lat)
    common_sites.scatter(x, y, c='r', marker='o', s=s_common, alpha=alpha_common)

    # Plot labels
    title = '%s Site Prediction %s,\nRed=Discovered Sites\nBlue=Predicted Sites' % (country, model_name)

    plt.title(title)
    plt.xlabel('\n\n\nLongitude')
    plt.ylabel('Latitude\n\n\n')
    
    plt.show()
    return
