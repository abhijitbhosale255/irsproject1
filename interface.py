from flask import Flask,jsonify,request
import config
from project_app.utils import SpeciesType

app = Flask(__name__)

@app.route('/') #home api
def home():
    return "Welcome to home page"

@app.route('/predict_iris') #prediction api
def predict_iris():
    input_data = request.get_json()
    sepal_length=input_data['sepal_length']
    sepal_width=input_data['sepal_width']
    petal_length=input_data['petal_length']
    petal_width=input_data['petal_width']

    species = SpeciesType(sepal_length,sepal_width,petal_length,petal_width)
    iris_type = species.predict_target()

    return jsonify ({"Result": f"Predicted Iris flower type is :{iris_type}"})



if __name__ == '__main__':
    app.run(debug=True)