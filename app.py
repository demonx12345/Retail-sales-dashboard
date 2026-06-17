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
        query="""SELECT Sub_Category,SUM(Revenue) as RevenueSQL FROM orders GROUP BY Sub_Category ORDER BY RevenueSQL DESC"""
        result=pd.read_sql(query,conn)
        st.dataframe(result)
        st.info("Answer generated using SQLite query execution")
    st.success(f"Highest Revenue Sub Category: {result.iloc[0]['Sub_Category']}")
    st.bar_chart(result.set_index("Sub_Category"))

with st.expander('Question 2: Which region generated the highest profit?'):
    method=st.radio('Select a method',['Python','SQL'],key='q2')
    if method=='Python':
        result=(df.groupby('Region')['Profit']
        .sum()
        .reset_index()
        .sort_values("Profit",ascending=False)
        .reset_index(drop=True))
        st.dataframe(result)
        st.info("Answer generated using Pandas DataFrame operations")
    elif method=='SQL':
        query="""SELECT Region,SUM(Profit) as ProfitSQL FROM orders GROUP BY Region ORDER BY ProfitSQL DESC"""
        result=pd.read_sql(query,conn)
        st.dataframe(result)
        st.info("Answer generated using SQLite query execution")
    st.success(f"Highest Profiting Region: {result.iloc[0]['Region']}")
    st.bar_chart(result.set_index("Region"))

with st.expander('Question 3: What are the top 10 products by quantity sold?'):
    method=st.radio('Select a method',['Python','SQL'],key='q3')
    if method=='Python':
        result=(df.groupby('Product_Id')['Quantity']
        .sum()
        .reset_index()
        .sort_values("Quantity",ascending=False)
        .head(10)
        .reset_index(drop=True))
        st.dataframe(result)
        st.info("Answer generated using Pandas DataFrame operations")
    elif method=='SQL':
        query="""SELECT Product_Id,SUM(Quantity) as QuantitySQL FROM orders GROUP BY Product_Id ORDER BY QuantitySQL DESC LIMIT 10"""
        result=pd.read_sql(query,conn)
        st.dataframe(result)
        st.info("Answer generated using SQLite query execution")
    st.success(f"Product with the highest quantity sold: {result.iloc[0]['Product_Id']}")
    st.bar_chart(result.set_index("Product_Id"))

with st.expander('Question 4: What is the average discount percentage by category?'):
    method=st.radio('Select a method',['Python','SQL'],key='q4')
    if method=='Python':
        result=(df.groupby('Category')['Discount_Percent']
        .mean()
        .reset_index())
        st.dataframe(result)
        st.info("Answer generated using Pandas DataFrame operations")
    elif method=='SQL':
        query="""SELECT Category,AVG(Discount_Percent) as Discount_PercentSQL FROM orders GROUP BY Category"""
        result=pd.read_sql(query,conn)
        st.dataframe(result)
        st.info("Answer generated using SQLite query execution")


with st.expander('Question 5: Which state placed the highest number of orders?'):
    method=st.radio('Select a method',['Python','SQL'],key='q5')
    if method=='Python':
        result=(df.groupby('State')['Order_Id']
        .count()
        .reset_index(name='Order_Count')
        .sort_values("Order_Count",ascending=False)
        .reset_index(drop=True))
        st.dataframe(result)
        st.info("Answer generated using Pandas DataFrame operations")
    elif method=='SQL':
        query="""SELECT State,COUNT(State) as Order_CountSQL FROM orders GROUP BY State ORDER BY Order_CountSQL DESC"""
        result=pd.read_sql(query,conn)
        st.dataframe(result)
        st.info("Answer generated using SQLite query execution")
    st.success(f"State with highest number of orders: {result.iloc[0]['State']}")
    st.bar_chart(result.set_index("State"))

with st.expander('Question 6: Which customer segment generated the highest revenue?'):
    method=st.radio('Select a method',['Python','SQL'],key='q6')
    if method=='Python':
        result=(df.groupby('Segment')['Revenue']
        .sum()
        .reset_index()
        .sort_values("Revenue",ascending=False)
        .reset_index(drop=True))
        st.dataframe(result)
        st.info("Answer generated using Pandas DataFrame operations")
    elif method=='SQL':
        query="""SELECT Segment,SUM(Revenue) as RevenueSQL FROM orders GROUP BY Segment ORDER BY RevenueSQL DESC"""
        result=pd.read_sql(query,conn)
        st.dataframe(result)
        st.info("Answer generated using SQLite query execution")
    st.success(f"Highest Revenue Segment: {result.iloc[0]['Segment']}")
    st.bar_chart(result.set_index("Segment"))

with st.expander('Question 1: What is the sub category with the highest revenue?'):
    method=st.radio('Select a method',['Python','SQL'],key='q7')
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

with st.expander('Question 1: What is the sub category with the highest revenue?'):
    method=st.radio('Select a method',['Python','SQL'],key='q8')
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

with st.expander('Question 1: What is the sub category with the highest revenue?'):
    method=st.radio('Select a method',['Python','SQL'],key='q9')
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

with st.expander('Question 1: What is the sub category with the highest revenue?'):
    method=st.radio('Select a method',['Python','SQL'],key='q10')
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