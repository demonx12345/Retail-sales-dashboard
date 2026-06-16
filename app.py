import pandas as pd
import streamlit as st
import sqlite3

conn=sqlite3.connect('retail.db')

df=pd.read_csv('orders.csv')
st.title('Retail Sales Dashboard')
df["Revenue"]=(df["List Price"]*df["Quantity"]*(1-df["Discount Price"]/100))
df["Profit"]=((df["List Price"]-df["cost price"])*df["Quantity"]*(1-df["Discount Price"]/100))

df.to_sql('orders', conn, if_exists='replace', index=False)

with st.expander('Question 1: What is the category with the highest revenue?'):
    method=st.radio('Select a method',['Python','SQL'],key='q1')
    if method=='Python':
        result=(df.groupby('Category')['Revenue']
        .sum()
        .reset_index()
        .sort_values("Revenue",ascending=False))
        st.dataframe(result)
    elif method=='SQL':
        query="""SELECT Category,SUM(Revenue) as Revenue FROM orders GROUP BY Category ORDER BY Revenue DESC"""
        result=pd.read_sql(query,conn)
        st.dataframe(result) 
