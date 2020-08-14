#!/usr/bin/env python
# coding: utf-8



# Dependencies
import json
from flask import Flask, request, jsonify
from sklearn.externals import joblib
from model import *
import traceback
import pandas as pd
import numpy as np
from flask import jsonify


# Your API definition
app = Flask(__name__)




@app.route('/predict', methods=['POST'])
def predict():
			Details = request.json
			print(type(Details))
			A=[]
			A.append(int(Details['online']))
			A.append(int(Details['book']))
			A.append(int(Details['valueRating']))
			A.append(int(Details['valueVote']))
			A.append(int(Details['cost']))
			for ele in Details['arrType']:
				A.append(ele)
			for ele in Details['arrCuisine']:
				A.append(ele)
			for ele in Details['arrLocation']:
				A.append(ele)
			dfNew=pd.DataFrame()
			K = 5
			neighbors = getNeighbors(A, K)
			for neighbor in neighbors:
				row=data.loc[df.Name==neighbor]
				dfNew=dfNew.append(row)
				dfNew=dfNew.drop_duplicates(subset="Name")
			listName=[]
			for i in dfNew.index:
				listName.append((dfNew.loc[i].to_json()))
			return (jsonify(listName))

if __name__ == '__main__':
		try:
			port = int(sys.argv[1]) # This is for a command-line input
		except:
			port = 12345 # If you don't provide any port the port will be set to 12345
		app.run(port=port, debug=True)


