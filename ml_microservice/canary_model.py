from flask import Flask, jsonify, request, render_template, Response
import json
import pandas as pd
import pickle
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB



app = Flask(__name__)


iris = datasets.load_iris()
x_train,x_test,y_train,y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=0)
loaded_model = GaussianNB()
loaded_model.fit(x_train,y_train)


def predict_data(data_dict):

	data = pd.DataFrame(data_dict,index=[0])
	prediction = loaded_model.predict_proba(data)
	return prediction.tolist()[0]


def is_data_correct(data):

	if len(data)==4:
		return True
	
	return False


@app.route('/predict',methods=['POST'])
def predict():

	response = Response(status=400, response="Information Error")
	try:
		data=request.get_json()
		print(data)

		if is_data_correct(data):
			prediction = {}
			prediction['Scores'] = predict_data(data)
			prediction['Input'] = data
			response = app.response_class(
				response=json.dumps(prediction),status=200)

			return response
	except Exception as ex:
		return Response(status=400,response=ex)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001,threaded=True)


 #To test 
 #curl -i -X POST -H "Content-Type:application/json" -d '{"s_1":5.9,"s_w":3,"p_1":5.1,"p_w":1.8}' 'http://0.0.0.0:5001/predict'