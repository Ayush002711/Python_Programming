import numpy as np
import pandas as pd
import matplotlib.pylab  as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn. metrics import mean_squared_error,r2_score

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
    
def main():
    MarvellousRegression("Advertising.csv")

if  __name__=="__main__":
    main()

    
    


    