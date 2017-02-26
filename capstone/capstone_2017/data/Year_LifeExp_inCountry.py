# python program to plot year on the x axis and lifeExp on the y-axis
# for a particular country

#python Year_LifeExp_inCountry.py	[1]in gapminder.csv
#									[2]in country of choice

import pandas as pd
import sys
from matplotlib import pyplot as plot
import numpy as numpy

countryofchoice = sys.argv[2]


def df_country(df,country):
	'''
	import pandadataframe and get subset of
	data that matches country
	'''
	df = pd.read_csv(df)
	df_countryofchoice = df[df["country"]==country]
	return df_countryofchoice

dfname = sys.argv[1]
newdf = df_country(sys.argv[1],countryofchoice)
print(newdf.head())
plot.scatter(newdf["year"],newdf["lifeExp"])
plot.show()


