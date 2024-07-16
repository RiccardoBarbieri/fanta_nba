import os
import logging
import json
import numpy
import joblib
import pandas as pd
from directory_tree import display_tree


def init():
    """
    This function is called when the container is initialized/started, typically after create/update of the deployment.
    You can write the logic here to perform init operations like caching the model in memory
    """
    global model_with_processing
    # AZUREML_MODEL_DIR is an environment variable created during deployment.
    # It is the path to the model folder (./azureml-models/$MODEL_NAME/$VERSION)
    # Please provide your model's folder name if there is one

    model_path = os.path.join(
        os.getenv("AZUREML_MODEL_DIR"), "lr_with_preprocessing.joblib"
    )
    # deserialize the model file back into a sklearn model
    model_with_processing = joblib.load(model_path)
    logging.info("Init complete")


def run(raw_data):
    """
    This function is called for every invocation of the endpoint to perform the actual scoring/prediction.
    In the example we extract the data from the json input and call the scikit-learn model's predict()
    method and return the result back
    """
    logging.info("model 1: request received")
    data = json.loads(raw_data)["data"]
    print(data)
    data = pd.DataFrame(data, index=[0])
    print(data)
    data['point_diff'] = data['pts_H'] - data['pts_A']
    features = data.drop(columns=['pts_H', 'pts_A', 'referee_id', 'point_diff', 'home_team', 'away_team', 'referee_name', 'winner', 'date', 'season'])
    target = data['point_diff']
    result = model_with_processing.predict(features)
    print(result)
    logging.info("Request processed")
    return result.tolist()

