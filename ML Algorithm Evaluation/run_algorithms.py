#!/usr/bin/python

import time

def calculate_metrics(y_test,Y_predicted):

	from sklearn import metrics
	from sklearn.metrics import classification_report,confusion_matrix

	accuracy = metrics.accuracy_score(y_test,Y_predicted)
	print "accuracy = "+str(round(accuracy * 100,2))+"%"

	confusion_mat = confusion_matrix(y_test,Y_predicted)

	print confusion_mat
	print confusion_mat.shape

	print "TP\tFP\tFN\tTN\tSensitivity\tSpecificity"
	for i in range(confusion_mat.shape[0]):
		# i means which class to choose to do one-vs-the-rest calculation
		# rows are actual obs whereas columns are predictions
		TP = round(float(confusion_mat[i,i]),2)  # correctly labeled as i
		FP = round(float(confusion_mat[:,i].sum()),2) - TP  # incorrectly labeled as i
		FN = round(float(confusion_mat[i,:].sum()),2) - TP  # incorrectly labeled as non-i
		TN = round(float(confusion_mat.sum().sum()),2) - TP - FP - FN
		print str(TP)+"\t"+str(FP)+"\t"+str(FN)+"\t"+str(TN),
		sensitivity = round(TP / (TP + FN),2)
		specificity = round(TN / (TN + FP),2)
		print "\t"+str(sensitivity)+"\t\t"+str(specificity)+"\t\t"


	f_score = metrics.f1_score(y_test,Y_predicted)
	print f_score

def neural_network(dataset,class_labels,test_size):

	import numpy as np
	import pandas as pd
	from sklearn.cross_validation import train_test_split
	from sklearn.neural_network import MLPClassifier
	

	X = pd.read_csv(dataset)
	Y = pd.read_csv(class_labels)
	X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size= test_size, random_state=42) 

	model = MLPClassifier(hidden_layer_sizes=(100), activation='logistic',random_state = 42)
	model.fit(X_train,y_train)
	Y_predicted = model.predict(X_test)
	
	
	return y_test,Y_predicted


def random_forests(dataset,class_labels,test_size):

	import numpy as np
	import pandas as pd
	from sklearn.cross_validation import train_test_split
	from sklearn.ensemble import RandomForestClassifier
	from sklearn import metrics
	X = pd.read_csv(dataset)
	Y = pd.read_csv(class_labels)
	X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size= test_size, random_state=42)   
	model = RandomForestClassifier(n_estimators = 5, criterion = 'entropy',random_state = 42)
	model.fit(X_train,y_train)
	Y_predicted = model.predict(X_test)
	
	return y_test,Y_predicted

def support_vector_machines(dataset,class_labels,test_size):

	import numpy as np
	from sklearn import svm
	import pandas as pd
	from sklearn.cross_validation import train_test_split

	X = pd.read_csv(dataset)
	Y = pd.read_csv(class_labels)
	X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size= test_size, random_state=42)  
	# 'rbf' value is the gaussian kernel, 'C' is the coefficient used for regularization during training	
	model = svm.SVC(kernel='rbf',C=2.0)
	model.fit(X_train,y_train)
	Y_predicted = model.predict(X_test)

	return y_test,Y_predicted

def main():

	dataset = "Dataset.csv"
	class_labels = "Target_Labels.csv"
	test_size = 0.3

	print "\nrunning neural networks..."
	start_time = time.time()
	y_test,Y_predicted = neural_network(dataset,class_labels,test_size)
	calculate_metrics(y_test,Y_predicted)
	end_time = time.time()
	print "runtime = "+str(end_time - start_time)+" seconds"

	print "\nrunning random forests..."
	start_time = time.time()
	y_test,Y_predicted = random_forests(dataset,class_labels,test_size)
	calculate_metrics(y_test,Y_predicted)
	end_time = time.time()
	print "runtime = "+str(end_time - start_time)+" seconds"

	print "\nrunning support vector machines..."
	start_time = time.time()
	y_test,Y_predicted = support_vector_machines(dataset,class_labels,test_size)
	calculate_metrics(y_test,Y_predicted)
	end_time = time.time()
	print "runtime = "+str(end_time - start_time)+" seconds"


if __name__ == '__main__':
	start_time = time.time()
	main()
	end_time = time.time()
	print "runtime = "+str(end_time - start_time)+" seconds"
