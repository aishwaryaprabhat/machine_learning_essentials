# Machine Learning Essenntials
A repository that will contain notes, sample code and cheatsheets related to machine learning. The repository is a work in progress.

Currently it contains material related to 

* Complete Data Science Project (Housing Price Prediction)
* Regression
* ML as Microservice: Deploying a ML model as a service using Flask, Docker and Kubernetes

## Complete Data Science Project (Housing Price Prediction)
**Objective**:
Build a model of housing prices in California using the California census data. The data comprises of features such has population, median income, median housing price. The goal is to build a model that can learn from this data and be able to predict the median housing price in any district (smallest geographical unit in our consideration).

The project follows and executes the following general plan of how to execute a Data Science project:

1. Frame the problem and look at the big picture.2. Get the data.3. Explore the data to gain insights.4. Prepare the data to better expose the underlying data patterns to Machine Learningalgorithms.5. Explore many different models and short-list the best ones.6. Fine-tune your models and combine them into a great solution.7. Present your solution.8. Launch, monitor, and maintain your system.

## Regression
This directory contains the following:

```
regression/
├── Linear Regression.docx
├── Linear Regression.pdf
└── Regression.ipynb
```

* `Linear Regression.pdf` and `Linear Regression.docx` contains theory/interview questions.
* `Regression.ipynb` contains code snippets and examples 

Topics covered include:

* Linear Regression
* Gradient Descent
* Polynomial Regression
* Ridge Regression
* LASSO Regression
* ElasticNet
* Logistic Regression
* Softmax Regression

## ML as Microservice
This part of the repository can be used as a quick tutorial or demo of how to deploy a trained machine learning model using Flask, Kubernetes and Docker.
The `ml_microservice` directory contains the following:

```
ml_microservice/
├── Train and Export Model.ipynb
├── asyncio_script.py
├── canary_model.py
├── docker_files
│   ├── docker-compose.yaml
│   ├── dockerfile_canary
│   └── dockerfile_iris
├── flask_app.py
├── iris_model.pkl
└── k8_files
    ├── canary-deployment.yaml
    ├── canary-svc.yaml
    ├── iris-deployment.yaml
    └── iris-svc.yaml
```

1. First a logistic regression model is trained on the IRIS dataset using `Train and Export Model.ipynb`
2. The model is exported as a pickle file `iris_model.pkl`
3. Canary test is simulated using `canary_model.py`
4. Both the main model and canary test model are deployed using Flask as in `flask_app.py` and Docker and Kubernetes
