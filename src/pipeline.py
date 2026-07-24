from src.data_ingestion import data_ingestion
from src.data_preprocessing import preprocessing
from src.model_building import model_building
from src.model_evaluation import model_evaluation

def run_pipeline():
    data = data_ingestion()
    X_train, X_test, y_train, y_test = preprocessing(data)
    model = model_building(X_train, y_train)
    model_evaluation(model, X_test, y_test)