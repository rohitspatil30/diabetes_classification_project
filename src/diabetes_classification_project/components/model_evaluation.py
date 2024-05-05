import os
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from urllib.parse import urlparse
import numpy as np
import joblib
from  diabetes_classification_project import logger
from diabetes_classification_project.utils.common import save_json
from diabetes_classification_project.entity.config_entity import ModelEvaluationConfig
from pathlib import Path

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self,actual, pred):
        f1= (f1_score(actual, pred))
        acc = accuracy_score(actual, pred)
        pre = precision_score(actual, pred)
        rec = recall_score(actual, pred)
        return np.round(f1, 2), np.round(acc, 2), np.round(pre, 2), np.round(rec, 2)

    
    def save_results(self):

        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]
        
        predicted_qualities = model.predict(test_x)

        (f1, acc, pre, rec) = self.eval_metrics(test_y, predicted_qualities)
        
        # Saving metrics as local
        scores = {
            "f1": f1,
            "accuracy": acc,
            "precision": pre,
            "recall": rec
        }
        save_json(path=Path(self.config.metric_file_name), data=scores)