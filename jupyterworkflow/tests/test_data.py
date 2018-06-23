from jupyterworkflow.data import get_bicycle_traffic_data
import pandas as pd

def test_bicycle_traffic_data():
    data = get_bicycle_traffic_data()
    assert all(data.columns == ['Total', 'East', 'West'])
    assert isinstance(data.index, pd.DatetimeIndex)
