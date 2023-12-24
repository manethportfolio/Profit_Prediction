# Initially app.py now application.py

from flask import Flask,request,render_template
import numpy as np
import pandas as pd
import os


from sklearn.preprocessing import StandardScaler
from src.pipelines.predict_pipeline import CustomData, PredictPipeline

# Entry point to the application
application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html') # It will go search for the template folder for the html file 

''' 
This route activates the function below it to start the pipeline 
'''
@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html') # this file contains data fields to do the prediction 
    else:
        data = CustomData(
            R_n_D_Spend=float(request.form.get('R_n_D_Spend')),
            Administration=float(request.form.get('Administration')),
            Marketing_Spend=float(request.form.get('Marketing_Spend')),
            State=request.form.get('State'),
        )

        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        return render_template('home.html',results=results[0])
    

if __name__=="__main__":
    app.run(host="0.0.0.0") 