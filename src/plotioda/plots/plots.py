import matplotlib.pyplot as plt
from emcpy.plots.plots import Scatter
from emcpy.plots.map_plots import MapScatter
from emcpy.plots import CreateMap, CreatePlot, VariableSpecs
from emcpy.plots.map_tools import Domain, MapProjection

__all__ = ['gen_figure']


def gen_figure(plot, obsspace):
    """
    factory to generate figure depending on type of plot

    Args:
        plot: dictionary containing configuration
        obsspace: IODA Python ObsSpace object

    Returns:
        fig: matplotlib figure object
    """
    plot_types = {
        'map_scatter': _map_scatter,
    }

    fig = plot_types[plot['type']](plot, obsspace)

    return fig


def _map_scatter(plot, obsspace):
    # plot a variable on a map
    print(plot)
    print(obsspace)
