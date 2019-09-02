import numpy
import pandas
import csv
from scipy import stats
from pandas import read_csv

with open('LAVerhiclesRFE.csv','r') as LA_file:
	dataframe = read_csv(LA_file)
	#Gets rid of null values
	dataframe = dataframe.dropna()
	#Gets rid of outliers
	dataframe = dataframe[(numpy.abs(stats.zscore(dataframe)) < 3).all(axis=1)]
	dataframe.to_csv ('cleanedCars.csv', index = None) 