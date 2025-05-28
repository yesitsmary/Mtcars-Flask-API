import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

df = pd.read_csv("mtcars.csv")
X = df.drop(columns=["mpg", "model"])
y = df["mpg"]

model = LinearRegression()
model.fit(X, y)

# Define the order of columns expected in input
col_order = list(X.columns)

def predict(dict_values):
    x_df = pd.DataFrame([dict_values])[col_order]
    y_pred = model.predict(x_df)[0]
    return y_pred
