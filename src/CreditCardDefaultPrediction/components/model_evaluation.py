import os
import sys
from sklearn.metrics import accuracy_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import pickle
from src.CreditCardDefaultPrediction.utils.utils import load_object


class ModelEvaluation:
    def __init__(self):
        pass

    def eval_metrics(self,actual, pred):
        acc_score = accuracy_score(actual, pred)# here is Accuracy Score
        return acc_score


    def initiate_model_evaluation(self,train_array,test_array):
        try:
            x_test,y_test=(test_array[:,:-1], test_array[:,-1])

            model_path=os.path.join("artifacts","model.pkl")
            model=load_object(model_path)

            # mlflow.set_registry_uri("https://dagshub.com/waralkarshayu/credit_card_default_prediction.mlflow")

            # tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
            # print(tracking_url_type_store)


            with mlflow.start_run():

                predicted_qualities = model.predict(x_test)

                (acc_score) = self.eval_metrics(y_test, predicted_qualities)

                mlflow.log_metric("Accuracy Score", acc_score)
                
                # This condition is for the dagshub
                # Model registry does not work with file store
                # if tracking_url_type_store != "file":

                    # Register the model
                    # There are other ways to use the Model Registry, which depends on the use case,
                    # please refer to the doc for more information:
                    # https://mlflow.org/docs/latest/model-registry.html#api-workflow 
                    # mlflow.sklearn.log_model(model, "model", registered_model_name="ml_model")
                # It is for local    
                # else:
                    # mlflow.sklearn.log_model(model, "model")

        except Exception as e:
            raise e
              