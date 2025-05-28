import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

df = pd.read_csv("mtcars.csv")
X = df.drop(columns=["mpg"])
y = df["mpg"]

model = LinearRegression()
model.fit(X, y)

# Define the order of columns expected in input
col_order = list(X.columns)

def predict(dict_values):
    x = np.array([float(dict_values[col]) for col in col_order])
    x = x.reshape(1, -1)
    y_pred = model.predict(x)[0]
    return y_pred
