import numpy
import pandas
import csv
from pandas import read_csv
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn import datasets, linear_model
from matplotlib import pyplot as plot
from sklearn.model_selection import KFold


with open('cleanedCars.csv','r') as LA_file:
	dataframe = read_csv(LA_file)
	dataframe = shuffle(dataframe)
	array = dataframe.values
	X = array[:,0:3]
	Y = array[:,3]
	#Splitting the training and test data
	XTrainData, XTestData, YTrainingData, YTestData = train_test_split(X, Y, test_size=0.8)
	#Building a decision tree with linear models as their nodes
	linearModel = linear_model.LinearRegression()
	model = linearModel.fit(XTrainData, YTrainingData)
	predictions = linearModel.predict(XTestData)
	plot.scatter(YTestData, predictions)
	plot.xlabel('True Values')
	plot.ylabel('Predictions')
	kf = KFold(n_splits = 10)
	scores = []
	scores.append(model.score(XTestData,YTestData))
	print("Price Prediction Accuracy % Using 10 Cross Fold Validation:", numpy.mean(scores)*100)
	print("Price Prediction Accuracy % Using Linear Model Prediction:", model.score(XTestData, YTestData)*100)
	print("Scatter Plot of Successful Predictions Will Now Show;")
	plot.show()
