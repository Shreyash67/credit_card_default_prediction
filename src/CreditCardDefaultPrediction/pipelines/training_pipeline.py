from src.CreditCardDefaultPrediction.components.data_ingestion import DataIngestion

import os
import sys
from src.CreditCardDefaultPrediction.logger import logging
from src.CreditCardDefaultPrediction.exception import customexception
import pandas as pd

obj=DataIngestion()

obj.initiate_data_ingestion()