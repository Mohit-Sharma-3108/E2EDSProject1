import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from src.datascience.entity.config_entity import ModelEvaluationConfig
from src.datascience.utils.common import save_json
from pathlib import Path

os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/mohit1d.lp/E2EDSProject1.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"] = "mohit1d.lp"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "9373733327493dd1ae55bf9e767a047779257c65"


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)

        return  rmse, mae, r2
    
    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        X_test = test_data.drop(columns=self.config.target_column)
        y_test = test_data[self.config.target_column]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_uri_type_store = urlparse(mlflow.get_tracking_uri()).scheme


        with mlflow.start_run():
            predicted_qualities = model.predict(X_test)

            (rmse, mae, r2) = self.eval_metrics(y_test, predicted_qualities)

            # Saving metrics in local as json
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            # Logging params and metrics in MLFLOW
            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2)

            # Model registry does not work with file store
            if tracking_uri_type_store != "file":
                
                # Register the model
                # There are other ways to use the Model Registry, depending on the use case.
                # Please refer to the documentation for more info
                # MLFLOW Model Registry -> Type this in Google
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticNetModel")
            else:
                mlflow.sklearn.log_model(model, "model")