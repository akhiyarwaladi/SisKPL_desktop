
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
import os
def tree_print(tree, feature_names):
	print(tree.tree_)
	print(feature_names)
	print(tree.tree_.feature)

def tree_to_code(tree, feature_names):

	'''
	Outputs a decision tree model as a Python function
	
	Parameters:
	-----------
	tree: decision tree model
		The decision tree to represent as a function
	feature_names: list
		The feature names of the dataset used for building the decision tree
	'''

	tree_ = tree.tree_
	feature_name = [
		feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
		for i in tree_.feature
	]
	print "def tree({}):".format(", ".join(feature_names))

	def recurse(node, depth):
		indent = "  " * depth
		if tree_.feature[node] != _tree.TREE_UNDEFINED:
			name = feature_name[node]
			threshold = tree_.threshold[node]
			print "{}if {} <= {}:".format(indent, name, threshold)
			recurse(tree_.children_left[node], depth + 1)
			print "{}else:  # if {} > {}".format(indent, name, threshold)
			recurse(tree_.children_right[node], depth + 1)
		else:
			print "{}return {}".format(indent, tree_.value[node])

	recurse(0, 1)

# In[2]:
def makeModel(dataPath, modelPath):

	data = pd.read_csv(dataPath)


	X = data.drop("kelas",1)
	Y = data["kelas"]

	# split data train and data testing
	from sklearn.model_selection import train_test_split
	X_train, X_test, Y_train, Y_test = train_test_split(
	  X,
	  Y,
	  test_size=0.2,
	  random_state = 42 )
	print(list(X_train))
	from sklearn.tree import DecisionTreeClassifier

	decTree = DecisionTreeClassifier()
	print("fitting data ..")
	#print(list(X_train))
	decTree.fit(X_train, Y_train)

	#tree_print(decTree, ['1','2','3'])

	prediksi = decTree.predict(X_test)
	from sklearn.metrics import accuracy_score
	akurasi = accuracy_score(prediksi, Y_test)

	strAkurasi = str(akurasi * 100)[0:5]

	print("saving model ..")
	from sklearn.externals import joblib
	joblib.dump(decTree, modelPath)

	from sklearn.externals.six import StringIO  
	import pydotplus
	from sklearn import tree
	dotfile = StringIO()
	tree.export_graphviz(decTree, out_file=dotfile, feature_names=X.columns, filled=True, rounded=True, special_characters=True)
	graph=pydotplus.graph_from_dot_data(dotfile.getvalue())
	graph.write_pdf(os.path.splitext(modelPath)[0] + "_decTree.pdf")
	return strAkurasi
