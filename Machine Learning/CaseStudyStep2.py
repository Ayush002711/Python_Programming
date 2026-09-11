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

##################################
# Step2 : Data Analysis(EDA)
##################################

print(Border)
print("Step2 : Data Analysis(EDA)")
print(Border)

print("Shape of Dataset :",df.shape)

print("Column Names:",list(df.columns))

print("Missing Values per column : ")
print(df.isnull().sum())

print("Class Distribution (species count)")
print(df["species"].value_counts())

print("Statistcal report of Dataset:")
print(df.describe())



