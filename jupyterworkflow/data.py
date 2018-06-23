import os
from urllib.request import urlretrieve
import pandas as pd

GREENWAY_URL = 'https://data.seattle.gov/api/views/47yq-6ugv/rows.csv?accessType=DOWNLOAD'
FREMONT_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

def get_bicycle_traffic_data(filename='fremont.csv', url=FREMONT_URL,
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

    # removed parameter parse_dates=True and used below to speed up processing
    data = pd.read_csv('fremont.csv', index_col='Date')
    try:
        data.index = pd.to_datetime(data.index, format='%m/%d/%Y %H:%M:%S %p')
    except TypeError:
        data.index = pd.to_datetime(data.index)

    data.columns = ['West', 'East']
    data['Total'] = data['West'] + data['East']
    return data
