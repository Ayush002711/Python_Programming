import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def main():
    Border="-"*40

    print(Border)
    print("Load the Data")
    print(Border)

    df=pd.read_csv("Mall_Customers.csv")

    print(Border)
    print("Dataset Loaded Succesfully")
    print(Border)
    print(df.head())

    print(Border)
    print("Missing Values")
    print(Border)
    print(df.isnull().sum())

    X=df[[
        "AnnualIncome","SpendingScore"
    ]]

    print(Border)
    print("Selected Features:")
    print(Border)
    print(df.head())

if __name__=="__main__":
    main()