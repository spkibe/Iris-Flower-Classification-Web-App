# Iris Flower Classification Web App

This is a Flask web application that allows users to classify iris flowers based on their sepal and petal dimensions. The classification is performed using a trained SVM model.

## Installation

1. Clone the repository:
```
git clone git@github.com:spkibe/Iris-Flower-Classification-Web-App.git
```
2. Navigate to the project directory:
```
cd iris-flower-classification
```
3. Build the Docker image:
```
docker build -t flask-app .
```
4. Run the Docker container:
```
docker run -p 5000:5000 flask-app
```
  
5. Open a web browser and navigate to *http://localhost:5000* to access the web app.

6. Usage
  > 1. Enter the sepal length, sepal width, petal length, and petal width of the iris flower into the input fields on the home page. <br>
  >  2. Click the "Predict" button to classify the iris flower.<br>
  > 3. The predicted species of the iris flower will be displayed on the web page.
           
