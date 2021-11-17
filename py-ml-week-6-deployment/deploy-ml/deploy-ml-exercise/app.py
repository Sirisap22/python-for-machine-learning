import pickle
with open('./iris_svm_classifier.pkl', 'rb') as file:
    model = pickle.load(file)

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/predict_iris/svm')
def predict_iris_svm():
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