import pandas as pd
import numpy as np

df = pd.read_csv("data.csv", header=None, encoding="ISO-8859-1")

df["Revenue"] = df["Quantity"] * df["UnitPrice"]

df.columns = [
    "InvoiceNo", "StockCode", "Description",
    "Quantity", "InvoiceDate", "UnitPrice",
    "CustomerID", "Country"
]
print(df.head())

print(df["Revenue"].sum())