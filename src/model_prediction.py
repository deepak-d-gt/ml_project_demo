import pandas as pd
import joblib

model = joblib.load("models/model.pkl")

prediction = pd.DataFrame(
    {
        "F1":[35],
        "F2": [40],
    }
)

predicted = model.predict(prediction)

print(predicted)