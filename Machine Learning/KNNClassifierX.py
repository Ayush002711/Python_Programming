import numpy as np
from sklearn.neighbors import KNeighborsClassifier

def main():
    X=np.array([
        [1,2],
        [2,3],
        [3,1],
        [5,6]    
    ])

    Y=np.array(["Red","Red","Blue","Blue"])

    new_point = np.array([[3,3]])

    print("Independent variables are :")
    print(X)



if __name__=="___main___":
    main()