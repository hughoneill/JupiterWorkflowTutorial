from jupyterworkflow.data import get_bicycle_traffic_data
import pandas as pd
import numpy as np

def test_bicycle_traffic_data():
    data = get_bicycle_traffic_data()
    assert all(data.columns == [ 'West','East','Total'])
    assert isinstance(data.index, pd.DatetimeIndex)
    assert len(np.unique(data.index.time) == 24)
