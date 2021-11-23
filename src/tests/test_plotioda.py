import numpy as np
import matplotlib.pyplot as plt
from emcpy.plots import CreateMap
from emcpy.plots.map_tools import Domain, MapProjection
from emcpy.plots.map_plots import MapScatter, MapGridded
import plotioda.io as io
import plotioda.configuration as piconfig
import plotioda.utils as piutils
import os
import sys


def test_plotioda_full():
    # test reading in YAML file and producing plots as specified

    # get full path of YAML file
    my_dir = os.path.dirname(__file__)
    filepath = os.path.join(my_dir, 'inputs', 'test_plot.yaml')
    yamlfile = piutils.get_full_path(filepath)

    # get configuration from YAML
    config = piconfig.get_config(yamlfile)
    print(config)
