import streamlit as st
import pandas as pd
import logging

from data_loader import *
from query_functions import *

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

st.title('Retail Sales Dashboard')
source = st.selectbox("Dataset Source",["Local CSV", "AWS S3"])
try:
    df = load_data(source)
except Exception:
    st.error("Dataset could not be loaded")
    st.stop()

df["Revenue"]=(df["List_Price"]*df["Quantity"]*(1-df["Discount_Percent"]/100))
df["Profit"]=((df["List_Price"]-df["cost_price"])*df["Quantity"]*(1-df["Discount_Percent"]/100))
df["Profit_Margin"]=(df["Profit"]/df["Revenue"])*100

conn = create_database(df)

def run_question(title,key,pandas_result,sql_query,success_text,index_column):
    with st.expander(title):
        method = st.radio("Select a method",["Python", "SQL"],key=key)
        if method == "Python":
            result = pandas_result
            st.info("Answer generated using Pandas DataFrame operations")
        else:
            result = pd.read_sql(sql_query, conn)
            st.info("Answer generated using SQLite query execution")
        st.dataframe(result)
        st.success(f"{success_text}: {result.iloc[0][index_column]}")
        st.bar_chart(result.set_index(index_column))

run_question(
    title="Question 1: What is the sub category with the highest revenue?",
    key="q1",
    pandas_result=q1_pandas(df),
    sql_query=Q1_SQL,
    success_text="Highest Revenue Sub Category",
    index_column="Sub_Category"
)
run_question(
    title="Question 2: Which region generated the highest profit?",
    key="q2",
    pandas_result=q2_pandas(df),
    sql_query=Q2_SQL,
    success_text="Highest Profiting Region",
    index_column="Region"
)
run_question(
    title="Question 3: What are the top 10 products by quantity sold?",
    key="q3",
    pandas_result=q3_pandas(df),
    sql_query=Q3_SQL,
    success_text="Product with the highest quantity sold",
    index_column="Product_Id"
)
run_question(
    title="Question 4: What is the average discount percentage by category?",
    key="q4",
    pandas_result=q4_pandas(df),
    sql_query=Q4_SQL,
    success_text="Top Average Discount Percentage by Category",
    index_column="Category"
)
run_question(
    title="Question 5: Which state placed the highest number of orders?",
    key="q5",
    pandas_result=q5_pandas(df),
    sql_query=Q5_SQL,
    success_text="State with highest number of orders",
    index_column="State"
)
run_question(
    title="Question 6: Which customer segment generated the highest revenue?",
    key="q6",
    pandas_result=q6_pandas(df),
    sql_query=Q6_SQL,
    success_text="Highest Revenue Segment",
    index_column="Segment"
)
run_question(
    title="Question 7: Which shipping mode is used most frequently?",
    key="q7",
    pandas_result=q7_pandas(df),
    sql_query=Q7_SQL,
    success_text="Most used Shipping Mode",
    index_column="Ship_Mode"
)
run_question(
    title="Question 8: What are the top 10 cities by revenue?",
    key="q8",
    pandas_result=q8_pandas(df),
    sql_query=Q8_SQL,
    success_text="City with highest revenue",
    index_column="City"
)
run_question(
    title="Question 9: Which Sub Categories have the highest profit margin?",
    key="q9",
    pandas_result=q9_pandas(df),
    sql_query=Q9_SQL,
    success_text="Sub Category with highest profit margin",
    index_column="Sub_Category"
)
run_question(
    title="Question 10: What is the State which generated the highest revenue?",
    key="q10",
    pandas_result=q10_pandas(df),
    sql_query=Q10_SQL,
    success_text="State with highest revenue",
    index_column="State"
)
conn.close()