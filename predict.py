import pandas as pd
import joblib

model = joblib.load("model/linreg_v-1.joblib")

def predict(**features):
    """
        features:
            - year
            - temp
            - atemp
            - casual 
            - registered
    """
    data = pd.DataFrame([features])
    pred = model.predict(data)[0]
    return int(pred)