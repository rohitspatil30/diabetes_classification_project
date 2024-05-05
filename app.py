from flask import Flask, render_template, request
import os 
import numpy as np
import pandas as pd
from diabetes_classification_project.pipeline.prediction import PredictionPipeline


app = Flask(__name__) # initializing a flask app


@app.route('/',methods=['GET'])  # route to display the home page
def homePage():
    return render_template("index.html")



@app.route('/train',methods=['GET'])  # route to train the pipeline
def training():
    os.system("python main.py")
    return "Training Successful!" 




@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            pregnancies=float(request.form['pregnancies'])
            glucose =float(request.form['glucose'])
            blood_pressure =float(request.form['blood_pressure'])
            skin_thickness =float(request.form['skin_thickness'])
            insulin =float(request.form['insulin'])
            bmi =float(request.form['bmi'])
            diabetes_pedigree_function =float(request.form['diabetes_pedigree_function'])
            age =float(request.form['age'])
                 
         
            data = [pregnancies,glucose,blood_pressure,skin_thickness,insulin,bmi,diabetes_pedigree_function,age]
            data = np.array(data).reshape(1, 8)
            
            obj = PredictionPipeline()
            predict = obj.predict(data)
            print(predict)

            return render_template('results.html', prediction = str(predict))

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    else:
        return render_template('index.html')



if __name__ == "__main__":
	app.run(host="0.0.0.0", port = 8080)