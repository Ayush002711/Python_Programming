import pandas as pd
import numpy as np
import joblib 

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix

#------------------------------------------------------------
#   FunctionName:  LoadData
#   Description :  Load the data from CSV
#   Input       :  Datapath
#   Output      :  Data Frame
#   Author      :  Ayush Ajit Jadhav
#   Date        :  16/08/2026
#------------------------------------------------------------

def LoadData(Datapath):
    df=pd.read_csv(Datapath)

    print("Dataset loaded Succedfully")
    print(df.head())

    return df

#------------------------------------------------------------
#   FunctionName:  Preproccesing Data
#   Description :  It perform Data Analysis
#   Input       :  Data frame
#   Output      :  Updated data frame
#   Author      :  Ayush Ajit Jadhav
#   Date        :  16/08/2026
#------------------------------------------------------------

def PreprocceData(df):
    df = df.drop([
        "Passengerid",
        "zero",
        "name"
    ],
    errors="ignore"
    )
    #Handle Missing Values
    df["Age"]=df["Age"].fillna(df["Age"].median())
    df["Fare"]=df["Fare"].fillna(df["Fare"].median())

    df["Embarked"]=df["Embarked"].fillna(df["Embarked"].mode()[0])

    #Convert Categorical to numeric data

    df=pd.get_dummies(
        df,
        columns=["Embarked"],
        drop_first=True,
        dtype=int
    )

    print(df.head())

    print("Data Preproccesing Completed")
    print(df)
#------------------------------------------------------------
#   FunctionName:  main
#   Description :  Entry point function
#   Input       :  None
#   Output      :  None
#   Author      :  Ayush Ajit Jadhav
#   Date        :  16/08/2026
#------------------------------------------------------------

def main():
    df=LoadData("MarvellousTitanicDataset.csv")
    
    df=PreprocceData(df)

if __name__=="__main__":
    main()