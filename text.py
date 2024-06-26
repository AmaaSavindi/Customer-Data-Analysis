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
    purchase = str(purchase).replace('"', '')
    parts = purchase.split(';')
    for part in parts:
        item_and_price = part.split(',')
        if len(item_and_price) == 2:  # Check if both item and price are present
            items.append(item_and_price[0].strip())

# Most Purchased top 3 Items
top_purchased_items = pd.Series(items).value_counts().nlargest(3)

# Generated total revenue
total_revenue = sum(float(p.split(',')[1]) for purchase in info['purchase_history'].fillna('').str.split(';') for p in purchase if len(p.split(',')) == 2)

# Average Purchase Per Customer
avg_purchase_per_customer = total_revenue / customers_num

# Identify Customers who Spent Above $100
highest_spending_customers = info[info['purchase_history'].apply(lambda x: sum(float(p.split(':')[1]) if len(p.split(':')) == 2 else 0 for p in str(x).split(';'))) > 100]['customer_id'].tolist()

# Find Customers who Purchased a Specific Item
specific_items_customer = info[info['purchase_history'].fillna('').str.contains('Product X')]['customer_id'].tolist()

# Group Customers by Location & Calculate Total Spending per Location
total_spending_per_location = info.groupby('location')['purchase_history'].apply(lambda x: sum(float(p.split(':')[1]) for p in str(x).split(';') if len(p.split(':')) == 2))

#Top 5 Purchased Items and their Quantities
import matplotlib.pyplot as plt

if not top_purchased_items.empty:
    top_purchased_items.plot(kind='bar', xlabel='Item', ylabel='Quantity', title='Top 5 Purchased Items')
    plt.show()
else:
    print("No data available to plot.")

# Print Results
print("Number of Customers:", customers_num)
print("Average Customer Age:", avg_age)
print("Number of Customers in a Specific Age Range (25-35 years old):", num_customers_age_range)
print("Top 3 Most Purchased Items:")
print(top_purchased_items)
print("Total Revenue Generated:", total_revenue)
print("Average Purchase Amount Per Customer:", avg_purchase_per_customer)
print("Identify Customers who Spent Above $100:", highest_spending_customers)
print("Find Customers who Purchased Product X:", specific_items_customer)
print("Total Spending per Location:")
print(total_spending_per_location)



