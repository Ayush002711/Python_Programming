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
    print("Selected Features")
    print(Border)
    print(df.head())

    Scaler=StandardScaler()

    X_Scaled=Scaler.fit_transform(X)

    print(Border)
    print("Scaled Data")
    print(X_Scaled[:5])
    print(Border)

    WCSS=[]

    for K in range(1,11):
        model=KMeans(n_clusters=K,random_state=42,n_init=10)
        model.fit(X_Scaled)

        WCSS.append(model.inertia_)

    print("Values of WCSS:")
    for i in range (len(WCSS)):
        print(f"{i+1}:{WCSS[i]}")

    plt.plot(range(1,11),WCSS,marker="o")
    plt.xlabel("Number of Clusters:")
    plt.ylabel("WCSS")
    plt.title("Marvellous Elbow Method")
    plt.grid(True)
    plt.show()

    model=KMeans(
        n_clusters=K,
        random_state=42,
        n_init=10
    )

    Clusters=model.fit_predict(X_Scaled)

    df["Clusters"]=Clusters

    print(Border) 
    print("Dataset with Clusters:")
    print(Border)
    print(df.head(21))
            
if __name__=="__main__":
    main()