from flask import Flask, request, jsonify
from flask.logging import create_logger
import logging

import pandas as pd
import joblib


app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)



@app.route("/")
def home():
    html = "<h3>Sklearn Prediction Home</h3>"
    return html

@app.route("/predict", methods=['POST'])
def predict():
    """Performs an sklearn prediction
        
        input looks like:
        {
        "CHAS":{
        "0":0
        },
        "RM":{
        "0":6.575
        },
        "TAX":{
        "0":296.0
        },
        "PTRATIO":{
        "0":15.3
        },
        "B":{
        "0":396.9
        },
        "LSTAT":{
        "0":4.98
        }
        
        result looks like:
        { "prediction": [ <val> ] }
        
        """
    
    # Logging the input payload
    json_payload = request.json
    LOG.info(f"JSON payload: \n{json_payload}")
    inference_payload = pd.DataFrame(json_payload)
    LOG.info(f"Inference payload DataFrame: \n{inference_payload}")
    # scale the input
    # get an output prediction from the pretrained model, clf
    prediction = list(clf.predict(inference_payload.values))
    LOG.info(f"Prediction: {prediction}")
    return jsonify({'prediction': prediction})

if __name__ == "__main__":
    # load pretrained model as clf
    clf = joblib.load("./model_data/boston_housing_prediction.pkl")
    app.run(host='0.0.0.0', port=80, debug=True) # specify port=80
