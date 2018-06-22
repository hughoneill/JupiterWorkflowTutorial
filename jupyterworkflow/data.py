import os
from urllib.request import urlretrieve
import pandas as pd

GREENWAY_URL = 'https://data.seattle.gov/api/views/47yq-6ugv/rows.csv?accessType=DOWNLOAD'

def get_bicycle_traffic_data(filename='greenway.csv', url=GREENWAY_URL,
                             force_download=False):
    """Download and cache Seattle bicycle traffic data (Greenway data default)

    Parameters
    ----------
    filename : string (optional)
        location to save the data
    url : string (optional)
        web location of the data
    force_download : bool (optional)
        if True, force redownload of data

    Returns
    -------
    data : pandas.DataFrame
        The Greenway bicycle counter data
    """
    if force_download or not os.path.exists(filename):
        urlretrieve(url, filename)
    data = pd.read_csv('greenway.csv', index_col='Date',parse_dates=True)
    data.columns = ('Total', 'East', 'West')
    return data
