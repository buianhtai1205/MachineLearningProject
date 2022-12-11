from sklearn import datasets, linear_model
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def  executeThisFunction():
    # height (cm), input Data, each row is a Data point
    X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T
    y = np.array([ 49, 50, 90, 54, 58, 59, 60, 62, 63, 64, 66, 67, 68])

    regr = linear_model.LinearRegression()
    regr.fit(X, y) # in scikit-learn, each sample is one row
    # Compare two results
    print("scikit-learn’s solution : w_1 = ", regr.coef_[0], "w_0 = ", regr.intercept_)
    st.write("scikit-learn’s solution : w_1 = ", regr.coef_[0], "w_0 = ", regr.intercept_)

    X = X[:,0]
    plt.plot(X, y, 'ro')
    a = regr.coef_[0]
    b = regr.intercept_
    x1 = X[0]
    y1 = a*x1 + b
    x2 = X[12]
    y2 = a*x2 + b
    x = [x1, x2]
    y = [y1, y2]


    plt.plot(x, y)
    st.pyplot(plt)

if __name__ == "__main__":
    executeThisFunction()