import pandas as pd
import streamlit as st
import sqlite3

conn=sqlite3.connect('retail.db')

df=pd.read_csv('orders.csv')
st.title('Retail Sales Dashboard')
df["Revenue"]=(df["List Price"]*df["Quantity"]*(1-df["Discount Price"]/100))
df["Profit"]=((df["List Price"]-df["cost price"])*df["Quantity"]*(1-df["Discount Price"]/100))

df.to_sql('orders', conn, if_exists='replace', index=False)

