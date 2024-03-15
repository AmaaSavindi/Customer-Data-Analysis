#Importing the libraries to read CSV and data manipulation
import pandas as pd

# Read the CSV file
info = pd.read_csv('CSV File for Task 02  (Medium) - CSV File for Task 02  (Medium).csv')

# No.of Customers
customers_num = len(info)

# Average Customer Age
avg_age = info['age'].mean()

# Number of Customers in a Specific Age Range (25-35 years old)
num_customers_age_range = len(info[(info['age'] >= 25) & (info['age'] <= 35)])

# Identify the items with the highest total purchase quantity
# Parse purchase history to get items and their quantities
items = []
for purchase in info['purchase_history']:
    item_purchases = purchase.split(';')
    for item in item_purchases:
        items.append(item.split(':')[0])

# Most Purchased top 3 Items
top_purchased_items = pd.Series(items).value_counts().nlargest(3)

# Generated total revenue
total_revenue = sum([float(p.split(':')[1]) for purchase in info['purchase_history'] for p in purchase.split(';')])

# Average Purchase Per Customer
avg_purchase_per_customer = total_revenue / customers_num

# Identify Customers who Spent Above $100
high_spending_customers = info[info['purchase_history'].apply(lambda x: sum(float(p.split(':')[1]) for p in x.split(';'))) > 100]['customer_id'].tolist()

# Find Customers who Purchased a Specific Item
customers_of_specific_item = info[info['purchase_history'].str.contains('Product X')]['customer_id'].tolist()

# Group Customers by Location & Calculate Total Spending per Location
total_spending_per_location = info.groupby('location')['purchase_history'].apply(lambda x: sum(float(p.split(':')[1]) for purchase in x.split(';')))

#Top 5 Purchased Items and their Quantities
import matplotlib.pyplot as plt

top_purchased_items.plot(kind='bar', xlabel='Item', ylabel='Quantity', title='Top 5 Purchased Items')
plt.show()




