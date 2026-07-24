from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from src.config import load_config

def preprocessing(data):

    config = load_config()

    print(config)
    print(type(config))

    X = data[["F1", "F2"]]
    y = data["T"]

    X_train, X_test, y_train,y_test = train_test_split(
        X,
        y,
        test_size = config["test_size"],
        random_state = 42
    )

    

    return X_train, X_test, y_train, y_test



