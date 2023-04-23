import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from shapely.geometry import Point
import contextily as ctx


atl_map = gpd.read_file("F:/New folder/Desktop/visualization/shape/tl_2019_13_cousub.shp")
stats = pd.read_csv("F:/New folder/Desktop/visualization/datamodel1.csv")
geometry = [Point(xy)for xy in zip(stats['Longitude'], stats['Latitude'])]
gdf = gpd.GeoDataFrame(stats, geometry=geometry)
gdf = gpd.sjoin(gdf,atl_map,how='inner',op = 'within')
fig, ax = plt.subplots(figsize = (10,10))
minx, miny, maxx, maxy = gdf.total_bounds
ax.set_xlim(minx-0.1, maxx+0.1)
ax.set_ylim(miny-0.1, maxy+0.1)

atl_map.plot(ax=ax, color = 'gray')
im=gdf.plot(ax = ax,column = 'PredictedCount' ,
         cmap = 'Reds', 
         markersize = 100 ,
         alpha = 0.8,
         legend = True,
         legend_kwds = {'shrink':0.5, 'label' : "Order Amount"},
         edgecolor = 'k',)


ax.set_title('Heatmap of Atlanta')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
plt.show()















# import pandas as pd
# import geopandas as gpd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import contextily as ctx

# # Load the shapefile of Atlanta
# atlanta_shapefile = gpd.read_file("F:/New folder/Desktop/visualization/shape/tl_2019_13_cousub.shp")
# ctx.bounds2raster(-84.55, 33.6, -84.35, 33.8, 'atlanta_basemap.png', zoom=11, ll=True)

# # Load the data from the CSV file
# data = pd.read_csv("F:/New folder/Desktop/visualization/datamodel1.csv")

# # Convert the data to a GeoDataFrame
# geometry = gpd.points_from_xy(data['Longitude'], data['Latitude'])
# geo_data = gpd.GeoDataFrame(data, geometry=geometry)

# # Set the projection to EPSG 4326 (WGS84)
# geo_data.crs = 'EPSG:4326'
# atlanta_shapefile = atlanta_shapefile.to_crs('EPSG:4326')

# # Plot the heatmap on top of the Atlanta shapefile
# fig, ax = plt.subplots(figsize=(10, 10))
# sns.kdeplot(
#     data=geo_data,
#     x='Longitude',
#     y='Latitude',
#     cmap='viridis',
#     shade=True,
#     bw=0.1,
#     alpha=0.5,
#     ax=ax,
# )

# # Add the basemap using contextily
# ctx.add_basemap(
#     ax=ax,
#     url='atlanta_basemap.png',
#     crs='EPSG:4326',
# )


# # Show the plot
# plt.show()
