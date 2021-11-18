import numpy as np
import matplotlib.pyplot as plt
from emcpy.plots import CreateMap
from emcpy.plots.map_tools import Domain, MapProjection
from emcpy.plots.map_plots import MapScatter, MapGridded


def test_emcpy_cartopy_works():
    # Create scatter plot on CONUS domian
    mymap = CreateMap(figsize=(12, 8),
                      domain=Domain('conus'),
                      proj_obj=MapProjection('plcarr'))
    # Add coastlines
    mymap.add_features(['coastlines'])

    # generate a diagonal line across the US
    scatterobj = MapScatter(latitude=np.linspace(35, 50, 30),
                            longitude=np.linspace(-70, -120, 30),
                            data=np.linspace(200, 300, 30))
    # change colormap and markersize
    scatterobj.cmap = 'Blues'
    scatterobj.markersize = 25

    # Draw data onto map
    mymap.draw_data([scatterobj])

    # Add plot features
    mymap.add_colorbar(label='colorbar label',
                       label_fontsize=12, extend='neither')
    mymap.add_title(label='EMCPy Map', loc='center',
                    fontsize=20)
    mymap.add_xlabel(xlabel='longitude')
    mymap.add_ylabel(ylabel='latitude')

    # annotate some stats
    stats_dict = {
        'nobs': len(np.linspace(200, 300, 30)),
        'vmin': 200,
        'vmax': 300,
    }
    mymap.add_stats_dict(stats_dict=stats_dict)

    # return the figure from the map object
    fig = mymap.return_figure()

    # save figure as PNG
    fig.savefig('test_plot_map_scatter_conus.png')