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
    return df
#------------------------------------------------------------
#   FunctionName:  Split Data
#   Description :  It performs splitting activity
#   Input       :  Data Frame
#   Output      :  4 subsets for training and testing
#   Author      :  Ayush Ajit Jadhav
#   Date        :  16/08/2026
#------------------------------------------------------------

def SplitData(df):
    X=df.drop("Survived",axis=1)
    Y=df["Survived"]

    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

    print("Dataset Splitting completed Succesfully")

    return X_train,X_test,Y_train,Y_test
#------------------------------------------------------------
#   FunctionName:  Train Model
#   Description :  It performs Model training
#   Input       :  Training Features and labels
#   Output      :  Trained model
#   Author      :  Ayush Ajit Jadhav
#   Date        :  16/08/2026
#------------------------------------------------------------

def TrainModel(X_train,Y_train):
    model=LogisticRegression(max_iter=1000)

    model=model.fit(X_train,Y_train)

    print("Model trained Succesfully")

    return model
#------------------------------------------------------------
#   FunctionName:  Evaluate Model
#   Description :  It performs Model testing
#   Input       :  Model,testing data (Features and labels)
#   Output      :  None
#   Author      :  Ayush Ajit Jadhav
#   Date        :  16/08/2026
#------------------------------------------------------------

def EvaluateModel(model,Y_test,X_test):
    Y_pred=model.predict(X_test)

    Accuracy=accuracy_score(Y_test,Y_pred)

    print("Accuracy is :",Accuracy)

    print("Confusion Matrix:",Y_test,Y_pred)

#------------------------------------------------------------
#   FunctionName:  Preserve Model
#   Description :  It performs Model preservation into .pkl file 
#   Input       :  Model
#   Output      :  None
#   Author      :  Ayush Ajit Jadhav
#   Date        :  16/08/2026
#-----------------------------------------------------------

def PreserveModel(model,Datapath):
    joblib.dump(model,Datapath)

    print("Model preserved with name:",Datapath)


def main():
    #Step:1
    df=LoadData("MarvellousTitanicDataset.csv")

    #Step:2
    df=PreprocceData(df)

    #Step:3
    X_train,X_test,Y_train,Y_test=SplitData(df)

    #Step:4
    model=TrainModel(X_train,Y_train)

    #Step:5
    EvaluateModel(model,Y_test,X_test)

    #Step:6
    PreserveModel(model,"MarvellousTitanic.pkl")

if __name__=="__main__":
    main()