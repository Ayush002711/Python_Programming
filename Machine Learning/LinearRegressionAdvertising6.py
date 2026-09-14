import numpy as np
import pandas as pd
import matplotlib.pylab  as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn. metrics import mean_squared_error,r2_score
from sklearn.model_selection import train_test_split

def MarvellousRegression(Datapath):
    Border="-"*40

    print(Border)
    print("Step 1 :Load the Dataset")
    print(Border)

    df=pd.read_csv(Datapath)

    print(df.head())

    print(Border)
    print("Step 2 : Remove unwanted columns")
    print(Border)

    if "Unnamed : 0" in df.columns:
        df=df.drop(columns=["Unwanted : 0"])

    print(Border)
    print("Step 3 : Check Missing Values")
    print(Border)

    print("Total Missing Values")
    print(Border)
    print(df.isnull().sum())


    print(Border)
    print("Step 4 :Statistical Summary ")
    print(Border)
    
    print(df.describe())

    print(Border)
    print("Step 5 :Correlation ")
    print(Border)

    print(df.corr())

    print(Border)
    print("Step 6 : Split Independent and Dependent")
    print(Border)

    X=df[["TV","radio","newspaper"]]
    Y=df["sales"]

    print(Border)
    print("Independent Variables")
    print(Border)
    print(df.head())

    print(Border)
    print("Dependent Variables")
    print(Border)
    print(df.tail())

    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

    print("Training Data :",X_train.shape)
    print("Testing  Data :",X_test.shape)

def main():
    MarvellousRegression("Advertising.csv")

if  __name__=="__main__":
    main()

    
    


    