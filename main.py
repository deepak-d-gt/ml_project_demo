import os

from src.data_ingestion import data_ingestion
from src.data_preprocessing import preprocessing
from src.model_building import model_building
from src.model_evaluation import model_evaluation

def main():
    data = data_ingestion()
    print(data)
    X_train, X_test, y_train, y_test = preprocessing(data)
    print(X_train,y_train,X_test,y_test)
    print("X_train shape:", X_train.shape)
    print("y_train shape:", y_train.shape)
    print("X_test shape :", X_test.shape)
    print("y_test shape :", y_test.shape)
    model = model_building(X_train,y_train)
    rmse, mape = model_evaluation(model, X_test,y_test)
    print(rmse)

if __name__ == "__main__":
    main()