def q1_pandas(df):
    return (df.groupby('Sub_Category')['Revenue']
        .sum()
        .reset_index()
        .sort_values("Revenue",ascending=False)
        .reset_index(drop=True))
def q2_pandas(df):
    return (df.groupby('Region')['Profit']
        .sum()
        .reset_index()
        .sort_values("Profit",ascending=False)
        .reset_index(drop=True))
def q3_pandas(df):
    return (df.groupby('Product_Id')['Quantity']
        .sum()
        .reset_index()
        .sort_values("Quantity",ascending=False)
        .head(10)
        .reset_index(drop=True))
def q4_pandas(df):
    return (df.groupby('Category')['Discount_Percent']
        .mean()
        .reset_index())
def q5_pandas(df):
    return (df.groupby('State')['Order_Id']
        .count()
        .reset_index(name='Order_Count')
        .sort_values("Order_Count",ascending=False)
        .reset_index(drop=True))
def q6_pandas(df):
    return (df.groupby('Segment')['Revenue']
        .sum()
        .reset_index()
        .sort_values("Revenue",ascending=False)
        .reset_index(drop=True))
def q7_pandas(df):
    return (df.groupby('Ship_Mode')['Order_Id']
        .count()
        .reset_index(name='Order_Count')
        .sort_values("Order_Count",ascending=False)
        .reset_index(drop=True))
def q8_pandas(df):
    return (df.groupby('City')['Revenue']
        .sum()
        .reset_index()
        .sort_values("Revenue",ascending=False)
        .head(10)
        .reset_index(drop=True))
def q9_pandas(df):
    return (df.groupby('Sub_Category')['Profit_Margin']
        .mean()
        .reset_index()
        .sort_values("Profit_Margin",ascending=False)
        .reset_index(drop=True))
def q10_pandas(df):
    return (df.groupby('State')['Revenue']
        .sum()
        .reset_index()
        .sort_values("Revenue",ascending=False)
        .reset_index(drop=True))
        
Q1_SQL ="""SELECT Sub_Category,SUM(Revenue) as RevenueSQL FROM orders GROUP BY Sub_Category ORDER BY RevenueSQL DESC"""
Q2_SQL ="""SELECT Region,SUM(Profit) as ProfitSQL FROM orders GROUP BY Region ORDER BY ProfitSQL DESC"""
Q3_SQL ="""SELECT Product_Id,SUM(Quantity) as QuantitySQL FROM orders GROUP BY Product_Id ORDER BY QuantitySQL DESC LIMIT 10"""
Q4_SQL ="""SELECT Category,AVG(Discount_Percent) as Discount_PercentSQL FROM orders GROUP BY Category"""
Q5_SQL ="""SELECT State,COUNT(State) as Order_CountSQL FROM orders GROUP BY State ORDER BY Order_CountSQL DESC"""
Q6_SQL ="""SELECT Segment,SUM(Revenue) as RevenueSQL FROM orders GROUP BY Segment ORDER BY RevenueSQL DESC"""
Q7_SQL ="""SELECT Ship_Mode,COUNT(Ship_Mode) as Order_CountSQL FROM orders WHERE Ship_Mode IS NOT NULL GROUP BY Ship_Mode ORDER BY Order_CountSQL DESC"""
Q8_SQL ="""SELECT City,SUM(Revenue) as RevenueSQL FROM orders GROUP BY City ORDER BY RevenueSQL DESC LIMIT 10"""
Q9_SQL ="""SELECT Sub_Category,AVG(Profit_Margin) as Profit_MarginSQL FROM orders GROUP BY Sub_Category ORDER BY Profit_MarginSQL DESC"""
Q10_SQL ="""SELECT State,SUM(Revenue) as RevenueSQL FROM orders GROUP BY State ORDER BY RevenueSQL DESC"""

