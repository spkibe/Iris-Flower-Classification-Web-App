from flask import Flask, request, jsonify, render_template, redirect, url_for
import pickle
import numpy as np

app = Flask(__name__)

# Load the pickled model
with open('svm_model.pkl', 'rb') as f:
    classifier = pickle.load(f)

# Create a dictionary to map numeric labels to species names
label_to_species = {0: 'Iris-setosa', 1: 'Iris-versicolor', 2: 'Iris-virginica'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form
    sepal_length = float(data['sepal_length'])
    sepal_width = float(data['sepal_width'])
    petal_length = float(data['petal_length'])
    petal_width = float(data['petal_width'])
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = classifier.predict(features)
    predicted_species = label_to_species[int(prediction[0])]  # Map numeric label to species name
    return render_template('index.html', prediction=predicted_species)



@app.route('/redirect', methods=['GET', 'POST'])
def redirect_home():
    return redirect(url_for('/'))

if __name__ == '__main__':
    app.run(debug=True)