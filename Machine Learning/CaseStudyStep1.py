import pandas as pd

Border ="-"*30

##################################
# Step1 : Load the Dataset
##################################

print(Border)
print("Step1 : Load the Dataset")
print(Border)

DataPath="iris.csv"

df=pd.read_csv(DataPath)

print("Dataset Loaded Sucessfully")
print("Initial entries from Dataset are :")
print(df.head())