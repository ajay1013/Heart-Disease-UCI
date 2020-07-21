# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 23:49:03 2020

@author: Ajay Kumar
"""


from flask import Flask, request
import pickle
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

pickle_in=open("classifier_heart.pkl", "rb")
classifier=pickle.load(pickle_in)

@app.route("/")
def welcome():
    return  "welcome everyone"

    
@app.route("/predict", methods=["GET"])
def Heart_patient_prediction():
    
    """Let's Authenticate whether a person has heart problem or not
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: age
        in: query
        type: number
        required: true
        
      - name: sex
        in: query
        type: number
        required: true
        
      - name: cp
        in: query
        type: number
        required: true
        
      - name: trestbps
        in: query
        type: number
        required: true
        
      - name: chol
        in: query
        type: number
        required: true
        
      - name: fbs
        in: query
        type: number
        required: true
        
      - name: restecg
        in: query
        type: number
        required: true
        
      - name: thalach
        in: query
        type: number
        required: true
        
      - name: exang
        in: query
        type: number
        required: true
        
      - name: oldpeak
        in: query
        type: number
        required: true

      - name: slope
        in: query
        type: number
        required: true
        
      - name: ca
        in: query
        type: number
        required: true
        
      - name: thal
        in: query
        type: number
        required: true
        
    responses:
        200:
            description: The output values
        
    """
    
    age=request.args.get("age")
    sex=request.args.get("sex")
    cp=request.args.get("cp")
    trestbps=request.args.get("trestbps")
    chol=request.args.get("chol")
    fbs=request.args.get("fbs")
    restecg=request.args.get("restecg")
    thalach=request.args.get("thalach")
    exang=request.args.get("exang")
    oldpeak=request.args.get("oldpeak")
    slope=request.args.get("slope")
    ca=request.args.get("ca")
    thal=request.args.get("thal")
    
    
    prediction=classifier.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    print(prediction)
    return "Hello The answer is " + str(prediction)

if __name__=="__main__":
    app.run()