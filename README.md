# Retail Sales Dashboard

## Overview

Retail Sales Dashboard is a Streamlit-based data analytics application built using Python, Pandas, SQLite, and AWS S3. The application analyzes a retail orders dataset and allows users to answer business questions using either Pandas operations or SQL queries.

The dashboard supports both local CSV files and cloud-hosted datasets stored in AWS S3.

---

## Features

* Interactive Streamlit dashboard
* Dual query execution methods:

  * Pandas DataFrame Operations
  * SQLite Queries
* AWS S3 Dataset Integration
* SQLite Database Creation from CSV Data
* Error Handling and Application Logging
* Data Visualization using Streamlit Charts
* Top 10 Business Analytics Queries

---

## Technologies Used

* Python 3.11
* Streamlit
* Pandas
* SQLite3
* AWS S3
* Git & GitHub

---

## Project Structure

```text
Retail-Sales-Dashboard/
│
├── .streamlit/
│   └── secrets.toml
│
├── app.py
├── data_loader.py
├── query_functions.py
│
├── orders.csv
├── requirements.txt
├── README.md
├── .gitignore
│
├── retail.db (generated automatically)
└── app.log (generated automatically)
```

---

## Module Responsibilities

### app.py

Handles:

* Streamlit User Interface
* Dashboard Layout
* User Interaction
* Question Rendering

### data_loader.py

Handles:

* Local CSV Loading
* AWS S3 Dataset Loading
* SQLite Database Creation

### query_functions.py

Contains:

* All Pandas Analysis Functions
* SQL Query Definitions
* Business Analytics Logic

---

## Dataset Source Options

### Local Dataset

```python
pd.read_csv("orders.csv")
```

### AWS S3 Dataset

```python
pd.read_csv(st.secrets["AWS_CSV_URL"])
```

---

## Calculated Metrics

### Revenue

Revenue = List Price × Quantity × (1 - Discount Percent / 100)

### Profit

Profit = (List Price - Cost Price) × Quantity × (1 - Discount Percent / 100)

### Profit Margin

Profit Margin = (Profit / Revenue) × 100

---

## Business Questions Answered

1. Which sub-category has the highest revenue?
2. Which region generated the highest profit?
3. What are the top 10 products by quantity sold?
4. What is the average discount percentage by category?
5. Which state placed the highest number of orders?
6. Which customer segment generated the highest revenue?
7. Which shipping mode is used most frequently?
8. What are the top 10 cities by revenue?
9. Which sub-categories have the highest profit margin?
10. Which state generated the highest revenue?

---

## Error Handling

The application includes exception handling for:

* Dataset loading failures
* AWS S3 connectivity issues
* Invalid file paths
* Database creation errors

---

## Logging

Application events are recorded in:

```text
app.log
```

Logged events include:

* Dataset loading
* Database creation
* Application execution status
* Error messages

---

## Deployment

The application can be deployed using:

* Streamlit Community Cloud
* AWS S3 for dataset hosting
* GitHub Repository Integration

---

## Author

Sanjeev Dayal
