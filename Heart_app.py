# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 16:28:05 2020

@author: dell
"""


import pickle
import numpy as np
from flask import Flask, request, render_template



app = Flask(__name__)

model = pickle.load(open('classifier_heart.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('Heart.html')

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    if prediction==1:
        return render_template('Heart.html', prediction_text='Sorry but you are likely to have a Heart disease')
    else:
        return render_template('Heart.html', prediction_text='Great you are safe as per your test results')

if __name__ == "__main__":
    app.run(port=12000)