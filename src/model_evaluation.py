import os
import mlflow
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error

def model_evaluation(model, X_test,y_test):

    y_pred = model.predict(X_test)

    rmse = mean_squared_error(y_test,y_pred)
    mape = mean_absolute_percentage_error(y_test, y_pred)

    mlflow.set_tracking_uri("sqlite:///mlflow.db")
    mlflow.set_experiment("My_Second_Experiment")

    with mlflow.start_run():

        mlflow.log_param("model_type", "LinearRegression")
        mlflow.log_param("test_size", 0.2)

        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("mape", mape)

    return rmse, mape

    

