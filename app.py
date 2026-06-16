import pandas as pd
import streamlit as st
import sqlite3

conn=sqlite3.connect('retail.db')

df=pd.read_csv('orders.csv')
st.title('Retail Sales Dashboard')
st.write(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
st.dataframe(df.head())

df.to_sql('orders', conn, if_exists='replace', index=False)

st.success('db created successfully')
query="SELECT count(*) FROM orders"
result=pd.read_sql(query,conn)
st.write(result)