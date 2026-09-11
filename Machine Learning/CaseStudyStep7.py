import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split 

from sklearn.tree import DecisionTreeClassifier

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

##################################
# Step3 : Decide Independent & Dependent Variables 
##################################

print(Border)
print("Step3 :Decide Independent & Dependent Variables ")
print(Border)

# X : Independent Variable / Features
# Y : Dependent Variable / Labels

Feature_cols=[
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)"
    ]   

X=df[Feature_cols]
Y=df["species"]

print("X Shape :",X.shape)
print("Y Shape :",Y.shape)

##################################
# Step4 : Visualization of Dataset
##################################

print(Border)
print("Step4 : Visualization of Dataset")
print(Border)

#Scatter Plot

plt.figure(figsize=(7,5))

for sp in df["species"].unique():
    temp =df[df["species"]==sp]
    plt.scatter(temp["petal length (cm)"],temp["petal width (cm)"],label=sp) 

plt.title("Marvellous Iris Case Study")

plt.xlabel("petal length (cm)")
plt.ylabel("petal width (cm)")

plt.legend()
plt.grid()
plt.show()

##################################
# Step5 : Split the Dataset for training and testing
##################################

print(Border)
print("Step5 :Split the Dataset for training and testing")
print(Border)

X_train, X_test, Y_train, Y_test =train_test_split(X,Y, test_size=0.5, random_state=42)

print("Dataset splitting activity done")

print("X : ",X.shape)  #(150,4)
print("Y :", Y.shape)  #(150,)
      
print("X_train :",X_train.shape)   #(75,4)
print("X_test :",X_test.shape)     #(75,4)

print("Y_train :",Y_train.shape)  #(75,)
print("Y_test :",Y_test.shape)    #(75,)

##################################
# Step6 : Build the Model
##################################

print(Border)
print("Step6 :Build the Model")
print(Border)

model=DecisionTreeClassifier(max_depth=5)

print("Model gets created succesfully")

##################################
# Step7 : Train the Model
##################################

print(Border)
print("Step7 :Train  the Model")
print(Border)

model.fit(X_train,Y_train)

print("Model trained succesfully")

