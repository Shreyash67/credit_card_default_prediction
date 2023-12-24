"""import os

path="notebooks/research.ipynb"

dir,file=os.path.split(path)

os.makedirs(dir,exist_ok=True)

with open(path,"w") as f:
    pass"""
    
    
from src.CreditCardDefaultPrediction.pipelines.prediction_pipeline import CustomData


custdataobj=CustomData(120000,2,2,2,26,-1,2,0,0,0,2,2682,1725,2682,3272,3455,3261,0,1000,1000,1000,0,2000)

data=custdataobj.get_data_as_dataframe()

print(data)