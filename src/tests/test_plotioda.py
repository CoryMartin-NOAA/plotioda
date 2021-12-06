import matplotlib
matplotlib.use('agg')
import plotioda.configuration as piconfig
import plotioda.utils as piutils
import plotioda.plots as piplots
import os


def test_plotioda_full():
    # test reading in YAML file and producing plots as specified

    # get full path of YAML file
    my_dir = os.path.dirname(__file__)
    filepath = os.path.join(my_dir, 'inputs', 'test_plot.yaml')
    yamlfile = piutils.get_full_path(filepath)

    # get configuration from YAML
    config = piconfig.get_config(yamlfile)

    # this test assumes only one plot will be generated
    # first make sure the YAML is as expected
    all_plots = config['plots']
    if len(all_plots) != 1:
        raise ValueError("YAML issue: total number of all plots != 1")
    for plot in all_plots:  # should only be one to loop through
        # check a few variables, not all
        if plot['type'] != 'map_scatter':
            raise ValueError("YAML issue: type should be 'map_scatter'")
        if plot['channel'] != 3:
            raise ValueError("YAML issue: channel should be 3")
        if not plot['stats']:
            raise ValueError("YAML issue: stats should be true")
        # call the factory and generate the plot based on the config
        myfig = piplots.gen_figure(plot)
        myfig.savefig(piutils.get_full_path(plot['outfile']))
