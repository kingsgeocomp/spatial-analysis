import os
import random
import pandas as pd
import seaborn as sb
import geopandas as gpd

random.seed(123456789)

df = pd.read_csv(os.path.join('data','airbnb-2016-Feb','listings-summary.csv.gz'))

df.columns

df.head(2)

df.shape

%pylab inline

print("Mean price: " + str(df.price.mean()))
print("Mean number of reviews: " + str(df.number_of_reviews.mean()))

sb.distplot(df.price)

sb.distplot(df.number_of_reviews)

sb.distplot(df.availability_365)

df.neighbourhood.unique()

from shapely.geometry import Point
crs = None
geometry = [Point(xy) for xy in zip(df.longitude, df.latitude)]
gdf = gpd.GeoDataFrame(df, crs=crs, geometry=geometry)
gdf.crs = {'init' :'epsg:27700'}
gdf.head()
gdf.plot()
