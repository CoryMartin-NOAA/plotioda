import pandas as pd
import numpy as np
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
    # get map dataframe
    df = _gen_map_df(plot, obsspace)
    print(df)

    # define map domain/projection based off of YAML
    domain = Domain(plot.get('domain', 'global'))
    proj = MapProjection(plot.get('projection', 'plcarr'))

    # generate map and add features
    mymap = CreateMap(figsize=(12, 8), domain=domain, proj_obj=proj)
    mymap.add_features(plot.get('features', ['coastlines']))

    # generate data to plot and set plotting attributes
    plotobj = MapScatter(df['latitude'], df['longitude'], df['variable'])
    for attr in ['cmap', 'vmin', 'vmax']:
        if attr in plot:
            setattr(plotobj, attr, plot[attr])

    # draw data on map
    mymap.draw_data([plotobj])

    # add titles, color bar, etc.
    mymap.add_colorbar(label=plot.get('colorbar label', ''),
                       label_fontsize=12, extend='neither')
    mymap.add_title(label=plot.get('title', ''),
                    loc='left', fontsize=12)
    mymap.add_title(label=plot.get('cycle string', ''),
                    loc='right', fontsize=12,
                    fontweight='semibold')
    mymap.add_xlabel(xlabel='Longitude')
    mymap.add_ylabel(ylabel='Latitude')

    # add a lat/lon grid if requested
    if 'grid' in plot and plot['grid']:
        mymap.add_grid()

    # add stats to the plot if requested
    if 'stats' in plot and plot['stats']:
        stats_dict = {
            'nobs': len(df['latitude']),
            'min': str(np.round(np.nanmin(df['variable']), 4)),
            'mean': str(np.round(np.nanmean(df['variable']), 4)),
            'max': str(np.round(np.nanmax(df['variable']), 4)),
        }
        mymap.add_stats_dict(stats_dict=stats_dict)

    return mymap.return_figure()


def _gen_map_df(plot, obsspace):
    # grab lat, lon, and requested variable
    df_dict = {}
    df_dict['latitude'] = obsspace.get_var('latitude', 'MetaData')
    df_dict['longitude'] = obsspace.get_var('latitude', 'MetaData')
    data = obsspace.get_var(plot['variable'], plot['group'])
    if plot['variable'] == 'brightness_temperature' and 'channel' in plot:
        # this is getting a brightness temperature channel
        chanCoords = _get_indexed_channels(obsspace)
        chanIndex = chanCoords.index(plot['channel'])
        df_dict['variable'] = data[:, chanIndex]
    else:
        # just grab the standard variable
        df_dict['variable'] = data
    # create the dataframe
    df = pd.DataFrame(df_dict)
    df = df.dropna().reset_index()  # remove NaNs

    return df


def _get_indexed_channels(obsspace):
    """
    Grab list of all channels from obs space.
    """
    chansCoords = obsspace.get_var('nchans', None)
    chansCoords = [int(i) for i in chansCoords]

    return chansCoords


def _get_data(obsspace, variable):
    """
    Grabs data from provided obsspace for
    the requested variable
    """
    var = obsspace.Variable(variable)
    data = var.read_data()

    return data


def _get_var_units(obsspace, variable):
    """
    Grabs units attribute from the requested variable
    """
    var = obsspace.Variable(variable)
    units = var.read_attr('units')

    return units
