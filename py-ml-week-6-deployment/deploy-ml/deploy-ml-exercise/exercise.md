# Exercise

ให้สร้าง Iris Classifier โดยใช้ Support Vector Machines (SVM)  
และใช้ Flask สร้าง Web Service

# Guideline

## 1. สร้างไฟล์ model.ipynb (จะทำใน Google Colab แล้วค่อยดาวน์โหลดลงมาก็ได้) และ Train SVM Model

ใช้ข้อมูล iris จาก sklearn dataset 

```python
from sklearn.datasets import load_iris
iris = load_iris()
```

## 2. Export ข้อมูลโมเดลที่ทำเสร็จแล้วเป็นไฟล์ .pkl ด้วย pickle
```python
import pickle
with open('iris_svm_classifier.pkl', 'wb') as file:
    pickle.dump(model, file)
```

## 3. สร้าง Web Service ด้วย Flask

### 3.1 สร้างไฟล์ app.py

ใน app.py สร้าง url ใหม่ `/predict_iris/svm`

```python
--------------------------------------------------------------------------------
File: app.py
--------------------------------------------------------------------------------
+ | from flask import Flask
+ |
+ | app = Flask(__name__)
+ |
+ | @app.route('/predict_iris/svm')
+ | def predict_iris_svm():
+ |     return 'Hello World'
```

Start server โดยพิมพ์คำสั่ง `flask run` ในลงใน TERMINAL
```CMD
\> flask run
```

ลองเข้าไปที่ http://127.0.0.1:5000/predict_iris/svm

## 3.2 รับค่า parameters จาก URL

```python
--------------------------------------------------------------------------------
File: app.py
--------------------------------------------------------------------------------
  | from flask import Flask
+ | from flask import request
  |
  | app = Flask(__name__)
  |
  | @app.route('/predict_iris/svm')
  | def predict_iris_svm():
+ |     sepal_length = request.args.get('sepal_length')
+ |     sepal_width = request.args.get('sepal_width')
+ |     petal_length = request.args.get('petal_length')
+ |     petal_width = request.args.get('petal_width')
c |     return 'sepal length = ' + sepal_length
```

** เมื่อทำการแก้ไขโค๊ดให้กด Ctrl-C เพื่อหยุดการทำงานของ server และทำการ start server ใหม่ด้วยคำสั่ง  `flask run`

ลองเข้าไปที่ http://127.0.0.1:5000/predict_iris/svm?sepal_length=123  
ลองเข้าไปที่ http://127.0.0.1:5000/predict_iris/svm?sepal_length=abc  
ลองเข้าไปที่ http://127.0.0.1:5000/predict_iris/svm?sepal_length=hello

## 3.3 Import โมเดลของเราจากไฟล์ .pkl ด้วย pickle และใช้โมเดลในการทำนายผล

```python
--------------------------------------------------------------------------------
File: app.py
--------------------------------------------------------------------------------
+ | import pickle
+ | with open('./iris_svm_classifier.pkl', 'rb') as file:
+ |     model = pickle.load(file)
  |
  |
  | from flask import Flask
  | from flask import request
  |
  | app = Flask(__name__)
  |
  | @app.route('/predict_iris/svm')
  | def predict_iris_svm():
  |     sepal_length = request.args.get('sepal_length')
  |     sepal_width = request.args.get('sepal_width')
  |     petal_length = request.args.get('petal_length')
  |     petal_width = request.args.get('petal_width')
+ |
+ |     unknown_iris = [sepal_length, sepal_width, petal_length, petal_width]
+ |     prediction = model.predict([unknown_iris])[0]
+ |     
+ |     if prediction == 0:
+ |         return 'Iris-Setosa'
+ |     elif prediction == 1:
+ |         return 'Iris-Versicolour'
+ |     elif prediction == 2:
+ |         return 'Iris-Virginica'
```

ลองเข้าไปที่ http://127.0.0.1:5000/predict_iris/svm?sepal_length=6.1&sepal_width=2.8&petal_length=4&petal_width=1.3  
ลองปรับตัวเลข sepal_lenght, sepal_width, petal_length, petal_width ใน url ดู