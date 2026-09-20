import pandas as pd

from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_squared_error

from sklearn.ensemble import BaggingRegressor

#------------------------------
# Step 1 : Load the Data
#------------------------------
Border="-"*40

df=pd.read_csv("california_housing.csv")

print(Border)
print("Shape of Dataset :",df.shape)
print(Border)
print("First Few Records :",df.head())
print(Border)

#--------------------------------------
# Step 2 :Seperate Features and Labels
#--------------------------------------

X=df.drop("target",axis=1)
Y=df["target"]

print("Shape of X",X.shape)
print("Shape of Y",Y.shape)

#-----------------------------------------------
# Step 3 :Split Dataset for training and testing
#-----------------------------------------------

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

#----------------------------------
# Step 4.1 : Create the Base Model
#----------------------------------

base_model=DecisionTreeRegressor(random_state=42)

#--------------------------------------
# Step 4.2 : Create the Bagging Model
#--------------------------------------

model=BaggingRegressor(
    estimator=base_model,
    n_estimators=10,
    random_state=42
)

#------------------------------
# Step 5 : Train  the Model
#------------------------------

model=model.fit(X_train,Y_train)

#------------------------------
# Step 6 : Test  the Model
#------------------------------

Y_pred=model.predict(X_test)

#---------------------------------
# Step 7 : Evaluate the Model
#---------------------------------

print(" MSE :",mean_squared_error(Y_test,Y_pred))
print("R2:",r2_score(Y_test,Y_pred))
print(Border)










