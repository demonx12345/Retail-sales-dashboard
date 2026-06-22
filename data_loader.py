import pandas as pd
import sqlite3
import logging
import streamlit as st

def load_data(source):
    try:
        if source == "Local CSV":
            df = pd.read_csv("orders.csv")
            logging.info("Loaded Local CSV")
        else:
            df = pd.read_csv(st.secrets["AWS_CSV_URL"])
            logging.info("Loaded AWS S3 Dataset")
        return df
    except Exception as e:
        logging.error(f"Dataset loading failed: {e}")
        raise

def create_database(df):
    conn = sqlite3.connect('retail.db')
    df.to_sql('orders',conn,if_exists='replace',index=False)
    logging.info("Orders table created successfully")
    return conn