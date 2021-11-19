import plotioda.io.IODA as IODA
import os

def test_ioda_read_data():
    # test reading in sample IODA file data
    
    # get path of test file from repo
    my_dir = os.path.dirname(__file__)
    input_file = os.path.join(my_dir, 'inputs', 'amsua_aqua_obs_2018041500.nc4')
    
    # attempt to open the file with IODA Python API
    my_ioda = IODA(input_file, name='Test Obs Space')
    
    lats = my_ioda.get_var('latitude', 'MetaData')
    lons = my_ioda.get_var('longitude', 'MetaData')
    tb = my_ioda.get_var('brightness_temperature', 'ObsValue')
    
    print(lats)
    print(lons)
    print(tb)
    print(lats.shape)
    print(tb.shape)