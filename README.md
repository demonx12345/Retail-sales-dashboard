# Retail Sales Dashboard

A Streamlit-based Retail Sales Analytics Dashboard that demonstrates data analysis using both Pandas and SQL.

## Features

- Load retail order data from CSV
- Store data in SQLite database
- Answer business questions using:
  - Pandas DataFrame operations
  - SQL queries
- Interactive Streamlit dashboard
- Visualizations using charts
- Cloud deployment through Streamlit Cloud

## Technologies Used

- Python
- Pandas
- SQLite
- Streamlit
- GitHub
- AWS S3 (Dataset Storage)

## Business Questions Answered

1. Which sub-category generated the highest revenue?
2. Which region generated the highest profit?
3. What are the top 10 products by quantity sold?
4. What is the average discount percentage by category?
5. Which state placed the highest number of orders?
6. Which customer segment generated the highest revenue?
7. Which shipping mode is used most frequently?
8. What are the top 10 cities by revenue?
9. Which sub-categories have the highest profit margin?
10. Which city generated the highest profit?

## Project Structure

```text
Retail-Sales-Dashboard/
│
├── .streamlit/
│   └── secrets.toml (contains AWS_CSV_URL)
│
├── app.py
├── orders.csv
├── requirements.txt
├── README.md
├── .gitignore
│
├── retail.db (auto-created)
└── app.log (auto-created)
```
### Notes

- `retail.db` is generated automatically when the application runs.
- `app.log` is generated automatically for logging and error tracking.
- `.streamlit/secrets.toml` stores the AWS S3 dataset URL and is excluded from Git using `.gitignore`.

## Running Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## Deployment

The application can be deployed using Streamlit Cloud.

## Author

Sanjeev Dayal
