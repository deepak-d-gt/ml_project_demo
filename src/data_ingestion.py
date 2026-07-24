import os
import pandas as pd
import numpy as np

from src.logger import logger



def data_ingestion():

    logger.info("Data Ingestion Started")


    data_path = os.path.join("data","Sample.csv")

    data = pd.read_csv(data_path)

    logger.info("Data Ingestion Completed")

    return data



