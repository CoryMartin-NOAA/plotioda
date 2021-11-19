import numpy as np
import plotioda.io as io
import os
import sys


def test_ioda_read_data():
    # test reading in sample IODA file data

    # get path of test file from repo
    my_dir = os.path.dirname(__file__)
    input_file = os.path.join(my_dir, 'inputs', 'amsua_aqua_obs_2018041500.nc4')

    # attempt to open the file with IODA Python API
    my_ioda = io.IODA(input_file, name='Test Obs Space')

    lats = my_ioda.get_var('latitude', 'MetaData')
    tb = my_ioda.get_var('brightness_temperature', 'ObsValue')

    # do some sanity checks
    if (lats.shape != (100,)):
        sys.exit(1)
    if (tb.shape != (100,15)):
        sys.exit(1)
    if (abs(np.nanmin(tb) - 202.71) > 0.1):
        sys.exit(1)
    if (abs(np.nanmax(tb) - 290.43) > 0.1):
        sys.exit(1)
