# Flask
# https://flask.palletsprojects.com/en/2.0.x/ 

from flask import Flask
from flask_cors import CORS
from flask import request

app = Flask(__name__)
CORS(app)

import pickle
with open('./iris_decision_tree_classifier.pkl', 'rb') as file:
    model = pickle.load(file)


@app.route('/predict_iris')
def predict_iris():
    sepal_length = request.args.get('sepal_length')
    sepal_width = request.args.get('sepal_width')
    petal_length = request.args.get('petal_length')
    petal_width = request.args.get('petal_width')

    unknown_iris = [sepal_length, sepal_width, petal_length, petal_width]
    prediction = model.predict([unknown_iris])[0]

    if prediction == 0:
        return 'Iris-Setosa'
    elif prediction == 1:
        return 'Iris-Versicolour'
    elif prediction == 2:
        return 'Iris-Virginica'
