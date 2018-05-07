import pandas as pd
import random

# Seed used for reproducibility
random.seed(42)

def randomSamplingFromDF(site_df, pred_df):
    """Obtain random samples from pred_df and call them
    samples that do not have neolithic sites in them
    
    Parameters
    ----------
        site_df : pandas.DataFrame
            dataframe of the common sites

        pred_df : pandas.DataFrame
            dataframe of the coordinates that will be used
            to predict whether a site exists at that
            coordinate or not
    """
    # sample len(site_df) number points from pred_df
    rand_sites = random.sample(xrange(len(pred_df)), len(site_df))
    rand_sites_sorted = list(reversed(sorted(rand_sites)))

    nonsite_df = pred_df.iloc[rand_sites_sorted]
    less_pred_df = pred_df.drop(rand_sites_sorted, axis=0)
    
    return (nonsite_df, less_pred_df)

def randomSamplingFromCSV(site_file, pred_file):
    """Obtain random samples from pred_df and call them
    samples that do not have neolithic sites in them
    
    Parameters
    ----------
        site_file : str
            string of the common sites csv

        pred_file : str
            string of the coordinates csv that 
            will be used to predict whether a
            site exists at that coordinate or not
    """
    site_df = pd.read_csv(site_file)
    pred_df = pd.read_csv(pred_file)

    # sample len(site_df) number points from pred_df
    rand_sites = random.sample(xrange(len(pred_df)), len(site_df))
    rand_sites_sorted = list(reversed(sorted(rand_sites)))

    nonsite_df = pred_df.iloc[rand_sites_sorted]
    less_pred_df = pred_df.drop(rand_sites_sorted, axis=0)
    
    return (nonsite_df, less_pred_df)