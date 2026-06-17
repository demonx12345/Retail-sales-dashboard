import pandas as pd
import streamlit as st
import sqlite3

conn=sqlite3.connect('retail.db')

df=pd.read_csv('orders.csv')
st.title('Retail Sales Dashboard')
df["Revenue"]=(df["List_Price"]*df["Quantity"]*(1-df["Discount_Percent"]/100))
df["Profit"]=((df["List_Price"]-df["cost_price"])*df["Quantity"]*(1-df["Discount_Percent"]/100))

df.to_sql('orders', conn, if_exists='replace', index=False)

with st.expander('Question 1: What is the sub category with the highest revenue?'):
    method=st.radio('Select a method',['Python','SQL'],key='q1')
    if method=='Python':
        result=(df.groupby('Sub_Category')['Revenue']
        .sum()
        .reset_index()
        .sort_values("Revenue",ascending=False)
        .reset_index(drop=True))
        st.dataframe(result)
        st.info("Answer generated using Pandas DataFrame operations")
    elif method=='SQL':
        query="""SELECT Sub_Category,SUM(Revenue) as Revenue FROM orders GROUP BY Sub_Category ORDER BY Revenue DESC"""
        result=pd.read_sql(query,conn)
        st.dataframe(result)
        st.info("Answer generated using SQLite query execution")
    st.success(f"Highest Revenue Sub Category: {result.iloc[0]['Sub_Category']}")
    st.bar_chart(result.set_index("Sub_Category"))
 