from sklearn.linear_model import LinearRegression

import os
import joblib

def model_building(X_train, y_train):

    model = LinearRegression()

    model.fit(X_train,y_train)

    os.makedirs("models", exist_ok=True)

    joblib.dump(model,"models/model.pkl")

    print("Model Saved Successfully")

    return model
