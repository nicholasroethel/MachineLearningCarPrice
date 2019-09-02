#Recursive Feature Elimination and Logistic Regression to get the most important attributes
import numpy
import pandas
from pandas import read_csv
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import warnings

with open('LAVerhiclesCondensed.csv','r') as LA_file:
	warnings.filterwarnings("ignore")
	#Adding labels and creating a pandas datafram
	features = ["year","odometer","lat","long","county_fips","state_fips","weather","price"]
	dataframe = read_csv(LA_file, names=features)
	# scaler = StandardScaler()
	array = dataframe.values
	#spllitting the target and attributes
	X = array[:,0:7]
	Y = array[:,7]
	array[:] = numpy.nan_to_num(array)
	#finding the 3 most importent attributes
	model = LogisticRegression(solver = 'lbfgs', multi_class='auto',max_iter=50)
	rfe = RFE(model, 3)
	fit = rfe.fit(X, Y)
	features.pop(7)
	print("The Features")
	print(features)
	print("How many features were chosen")
	print(fit.n_features_)
	print("If the feature was chosen")
	print(fit.support_)
	print("A ranking of the feature")
	print(fit.ranking_)
	x  = 0
	print("The 3 most importent attributes are: year, odometer and country_fips")