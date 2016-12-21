import pandas as pd
import seaborn as sb

df = pd.read_csv('~/Downloads/listings.csv')

df.columns

df.head(2)

%pylab inline

df.price.mean()
sb.distplot(df.price)

df.number_of_reviews.mean()
sb.distplot(df.number_of_reviews)
