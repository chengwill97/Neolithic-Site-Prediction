import os
import csv
import numpy  as np
import pandas as pd

import matplotlib

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


def plotPredictedFromDF(site_df, nonsite_df, model_name='prediction'):
    """Plot points of Ireland
    Parameters
    -----------
        site_df : pandas.DataFrame
            dataframe of the sites
        nonsite_df : pandas.DataFrame
            dataframe of the nonsites
            
    Returns
    --------
        None
    """
    country_df = site_df.where(site_df['country'] == 'Ireland')
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

    
    # Plot the geological features
    m = Basemap(projection='cyl',
                llcrnrlat=minlat,
                urcrnrlat=maxlat,     
                llcrnrlon=minlon,
                urcrnrlon=maxlon,
                resolution='i')

    m.drawparallels(np.arange(int(minlat),int(maxlat),1),labels=[1,0,0,0])
    m.drawmeridians(np.arange(int(minlon),int(maxlon),1),labels=[0,0,0,1])
    # m.fillcontinents(color='None')

    m.drawcoastlines()
    m.drawcountries()
    m.drawstates()
    # m.drawrivers()
    # m.fillcontinents(color='#04BAE3', lake_color='#FFFFFF')
    # m.drawmapboundary(fill_color='#FFFFFF')
    # m.bluemarble()

    # Plot ...site_prediction.csv scatterplots
    lat = np.array(nonsites_df['latitude'].tolist())
    lon = np.array(nonsites_df['longitude'].tolist())
    x, y = m(lon, lat)
    m.plot(x, y, 'b.', markersize=1)

    # Plot common_sites_V3.csv scatterplots
    lat = np.array(country_df['latitude'].tolist())
    lon = np.array(country_df['longitude'].tolist())
    x, y = m(lon, lat)
    m.plot(x, y, 'r.', markersize=1)

    # Plot labels
    title = 'Ireland Site Prediction %s,\nRed=Discovered Sites\nBlue=Predicted Sites' % (model_name)

    plt.title(title)
    plt.xlabel('\n\n\nLongitude')
    plt.ylabel('Latitude\n\n\n')
    
    plt.show()
    return


def plotPredictedFromCSV(site_file, nonsite_file):
    """Plot points of Ireland
    Parameters
    -----------
        sites_file : str
            string of site csv
        nonsite_file : string
            string of nonsite csv
            
    Returns
    --------
        None
    """
    country_df = pd.read_csv(site, sep=',', error_bad_lines=False)
    country_df = country_df.where(country_df['country'] == 'Ireland')
    nonsites_df = pd.read_csv(nonsite_file, sep=',', error_bad_lines=False)
    nonsites_df = nonsites_df.where(nonsites_df['prediction'] == 1)

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

    
    # Plot the geological features
    m = Basemap(projection='cyl',
                llcrnrlat=minlat,
                urcrnrlat=maxlat,     
                llcrnrlon=minlon,
                urcrnrlon=maxlon,
                resolution='i')

    m.drawparallels(np.arange(int(minlat),int(maxlat),1),labels=[1,0,0,0])
    m.drawmeridians(np.arange(int(minlon),int(maxlon),1),labels=[0,0,0,1])
    # m.fillcontinents(color='None')

    m.drawcoastlines()
    m.drawcountries()
    m.drawstates()
    # m.drawrivers()
    # m.fillcontinents(color='#04BAE3', lake_color='#FFFFFF')
    # m.drawmapboundary(fill_color='#FFFFFF')
    # m.bluemarble()

    # Plot ...site_prediction.csv scatterplots
    lat = np.array(nonsites_df['latitude'].tolist())
    lon = np.array(nonsites_df['longitude'].tolist())
    x, y = m(lon, lat)
    m.plot(x, y, 'b.', markersize=1)

    # Plot common_sites_V3.csv scatterplots
    lat = np.array(country_df['latitude'].tolist())
    lon = np.array(country_df['longitude'].tolist())
    x, y = m(lon, lat)
    m.plot(x, y, 'r.', markersize=1)

    # Plot labels
    plt.title('Ireland Site Prediction,\nRed=Discovered Sites\nBlue=Predicted Sites')
    plt.xlabel('\n\n\nLongitude')
    plt.ylabel('Latitude\n\n\n')
    
    plt.show()
    return