import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("data/retail_transactions_raw.csv")
df["Order_Date"]=pd.to_datetime(df["Order_Date"])
df["Customer_ID"]=df["Customer_ID"].fillna("Unknown")
df=df.drop_duplicates()
print("Total revenue: ₹{:,.2f}".format(df.Sales.sum()))
print("Orders:",df.Order_ID.nunique())
print("Unique customers:",df.loc[df.Customer_ID!="Unknown","Customer_ID"].nunique())
print("Top products:\n",df.groupby("Product").Sales.sum().sort_values(ascending=False).head(10))
monthly=df.groupby(df.Order_Date.dt.to_period("M")).Sales.sum(); monthly.plot(kind="bar",figsize=(10,5),title="Monthly Sales"); plt.tight_layout(); plt.show()
