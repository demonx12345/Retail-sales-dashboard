import pandas as pd
import streamlit as st
import sqlite3
import logging

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

conn=sqlite3.connect('retail.db')
logging.info("SQLite database connected")

st.title('Retail Sales Dashboard')
source = st.selectbox("Dataset Source",["Local CSV", "AWS S3"])
try:
    if source == "Local CSV":
        df = pd.read_csv("orders.csv")
        logging.info("Loaded Local CSV")
    else:
        df = pd.read_csv(st.secrets["AWS_CSV_URL"])
        logging.info("Loaded AWS S3 Dataset")

except Exception as e:
    logging.error(f"Dataset loading failed: {e}")
    st.error("Dataset could not be loaded")
    st.stop()

df["Revenue"]=(df["List_Price"]*df["Quantity"]*(1-df["Discount_Percent"]/100))
df["Profit"]=((df["List_Price"]-df["cost_price"])*df["Quantity"]*(1-df["Discount_Percent"]/100))
df["Profit_Margin"]=(df["Profit"]/df["Revenue"])*100

df.to_sql('orders', conn, if_exists='replace', index=False)
logging.info("Orders table created successfully")

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
    pandas_result=(df.groupby('Sub_Category')['Revenue']
        .sum()
        .reset_index()
        .sort_values("Revenue",ascending=False)
        .reset_index(drop=True)),
    sql_query="""SELECT Sub_Category,SUM(Revenue) as RevenueSQL FROM orders GROUP BY Sub_Category ORDER BY RevenueSQL DESC""",
    success_text="Highest Revenue Sub Category",
    index_column="Sub_Category"
)
run_question(
    title="Question 2: Which region generated the highest profit?",
    key="q2",
    pandas_result=(df.groupby('Region')['Profit']
        .sum()
        .reset_index()
        .sort_values("Profit",ascending=False)
        .reset_index(drop=True)),
    sql_query="""SELECT Region,SUM(Profit) as ProfitSQL FROM orders GROUP BY Region ORDER BY ProfitSQL DESC""",
    success_text="Highest Profiting Region",
    index_column="Region"
)
run_question(
    title="Question 3: What are the top 10 products by quantity sold?",
    key="q3",
    pandas_result=(df.groupby('Product_Id')['Quantity']
        .sum()
        .reset_index()
        .sort_values("Quantity",ascending=False)
        .head(10)
        .reset_index(drop=True)),
    sql_query="""SELECT Product_Id,SUM(Quantity) as QuantitySQL FROM orders GROUP BY Product_Id ORDER BY QuantitySQL DESC LIMIT 10""",
    success_text="Product with the highest quantity sold",
    index_column="Product_Id"
)
run_question(
    title="Question 4: What is the average discount percentage by category?",
    key="q4",
    pandas_result=(df.groupby('Category')['Discount_Percent']
        .mean()
        .reset_index()),
    sql_query="""SELECT Category,AVG(Discount_Percent) as Discount_PercentSQL FROM orders GROUP BY Category""",
    success_text="Top Average Discount Percentage by Category",
    index_column="Category"
)
run_question(
    title="Question 5: Which state placed the highest number of orders?",
    key="q5",
    pandas_result=(df.groupby('State')['Order_Id']
        .count()
        .reset_index(name='Order_Count')
        .sort_values("Order_Count",ascending=False)
        .reset_index(drop=True)),
    sql_query="""SELECT State,COUNT(State) as Order_CountSQL FROM orders GROUP BY State ORDER BY Order_CountSQL DESC""",
    success_text="State with highest number of orders",
    index_column="State"
)
run_question(
    title="Question 6: Which customer segment generated the highest revenue?",
    key="q6",
    pandas_result=(df.groupby('Segment')['Revenue']
        .sum()
        .reset_index()
        .sort_values("Revenue",ascending=False)
        .reset_index(drop=True)),
    sql_query="""SELECT Segment,SUM(Revenue) as RevenueSQL FROM orders GROUP BY Segment ORDER BY RevenueSQL DESC""",
    success_text="Highest Revenue Segment",
    index_column="Segment"
)
run_question(
    title="Question 7: Which shipping mode is used most frequently?",
    key="q7",
    pandas_result=(df.groupby('Ship_Mode')['Order_Id']
        .count()
        .reset_index(name='Order_Count')
        .sort_values("Order_Count",ascending=False)
        .reset_index(drop=True)),
    sql_query="""SELECT Ship_Mode,COUNT(Ship_Mode) as Order_CountSQL FROM orders WHERE Ship_Mode IS NOT NULL GROUP BY Ship_Mode ORDER BY Order_CountSQL DESC""",
    success_text="Most used Shipping Mode",
    index_column="Ship_Mode"
)
run_question(
    title="Question 8: What are the top 10 cities by revenue?",
    key="q8",
    pandas_result=(df.groupby('City')['Revenue']
        .sum()
        .reset_index()
        .sort_values("Revenue",ascending=False)
        .head(10)
        .reset_index(drop=True)),
    sql_query="""SELECT City,SUM(Revenue) as RevenueSQL FROM orders GROUP BY City ORDER BY RevenueSQL DESC LIMIT 10""",
    success_text="City with highest revenue",
    index_column="City"
)
run_question(
    title="Question 9: Which Sub Categories have the highest profit margin?",
    key="q9",
    pandas_result=(df.groupby('Sub_Category')['Profit_Margin']
        .mean()
        .reset_index()
        .sort_values("Profit_Margin",ascending=False)
        .reset_index(drop=True)),
    sql_query="""SELECT Sub_Category,AVG(Profit_Margin) as Profit_MarginSQL FROM orders GROUP BY Sub_Category ORDER BY Profit_MarginSQL DESC""",
    success_text="Sub Category with highest profit margin",
    index_column="Sub_Category"
)
run_question(
    title="Question 10: What is the State which generated the highest revenue?",
    key="q10",
    pandas_result=(df.groupby('State')['Revenue']
        .sum()
        .reset_index()
        .sort_values("Revenue",ascending=False)
        .reset_index(drop=True)),
    sql_query="""SELECT State,SUM(Revenue) as RevenueSQL FROM orders GROUP BY State ORDER BY RevenueSQL DESC""",
    success_text="State with highest revenue",
    index_column="State"
)
conn.close()