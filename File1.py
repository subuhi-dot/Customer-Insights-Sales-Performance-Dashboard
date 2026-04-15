from operator import index

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#Task:1 Import and clean the dataset, create useful calculated field and save cleaned file.
df = pd.read_csv("superstore_dataset.csv")

print(df.info())
print(df.isnull().sum())
df = df.dropna()
print(df.head())
df = df.drop_duplicates()
print(df.shape)
df["order_date"] = pd.to_datetime(df["order_date"])
df["ship_date"] = pd.to_datetime(df["ship_date"])
print(df.order_date )
print(df.ship_date )

#Total order value(total sales per order)
df['total_order_value'] = df['sales']*df['quantity']
print(df.total_order_value)

#profit margin
df['profit_margin']=df['profit']/df['sales']
print(df.profit_margin)

#Customer lifetime values
df['cus_lt_value']= df.groupby("customer")["sales"].transform('sum')
print(df.cus_lt_value)

#Days between purchases
df = df.sort_values(['customer', 'order_date'])
df['days_between_purchases'] = df.groupby('customer')['order_date'].diff()
print(df.days_between_purchases)
#saving clean data
df.to_csv('clean_superstore_dataset.csv')
df = pd.read_csv('clean_superstore_dataset.csv')
print(df.info())
df["order_date"] = pd.to_datetime(df["order_date"])
df["ship_date"] = pd.to_datetime(df["ship_date"])
print(df.info())
df.to_csv('my_clean_dataset.csv')
df=pd.read_csv('my_clean_dataset.csv')
print(df.head())





#Task:2
#Top selling products
#top_products = df.groupby("product_name")["sales"].sum()
#print(top_products.head())
#bar chart
#top_products.plot(kind='bar')
#plt.title('Top Selling Products')
#plt.xlabel('product_name')
#plt.ylabel('sales')
#plt.show()
#It shows the products with highest total sales.

#Top selling customer segment
#top_cus_segment=df.groupby('segment')['sales'].sum()
#print(top_cus_segment.head())
#bar chart
#segment_sales = df.groupby('segment')['sales'].sum()
#segment_sales.plot(kind='bar')
#plt.title('Sales by Customer Segment')
#plt.xlabel('segment')
#plt.ylabel('sales')
#plt.show()
#It shows the customer segment with highest sales. consumer segment produces more sales followed by corporate and home office.

#Monthly sales trend
#df['month'] = df['order_date'].dt.month
#monthly_sales = df.groupby('month')['sales'].sum()
#print(monthly_sales)
#line chart
#monthly_sales.plot()
#plt.title('Monthly Sales Trend')
#plt.xlabel('month')
#plt.ylabel('sales')
#plt.show()
#It shows monthly trend of sales. Highest sales months are November & December. Lowest sales months are January & February.

#outliers
#plt.scatter(df['sales'], df['profit'])
#plt.xlabel('sales')
#plt.ylabel('Profit')
#plt.title('Outliers')
#plt.show()
#Most orders have positive relationship b/w sales and profit but few orders show unusual pattern with high sales but loss.

#outliers=df[(df['profit']<0)]
#outliers=outliers[['sales','profit','discount','profit_margin']]
#print(outliers)

