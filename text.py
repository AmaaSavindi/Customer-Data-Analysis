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




