import numpy as np
import pandas as pd
import matplotlib.pylab  as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn. metrics import mean_squared_error,r2_score

def MarvellousRegression(Datapath):
    Border="_*40"

    print(Border)
    print("Step 1 :Load the Dataset")
    print(Border)

    df=pd.read_csv(Datapath)

    print(df.head())

def main():
    MarvellousRegression()

if  __name__=="__main__":
    main()
    