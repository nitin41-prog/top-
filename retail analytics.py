import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load dataset(Line no 26 and 27 )
# Preprocessing(Line no 29-33)
# 1. Profit margins by category and sub-category(Line no 37-45)
# 2. Sales and profit by state (Line no 47-56)
# 3. Discount impact on profit(Line no 58-66)
# 4. Loss-making products(Line no 68-70)
# 5. Average delivery time by ship mode(Line no 72-79)
# 6. Shipping mode frequency and profitability(Line no 81-83)
# 7. Shipping performance by region(Line no 85-87)
# 8. Average order value by segment(Line no 89-91)
# 9. Top 10 profitable customers(Line no 94-96)
# 10. Repeat customers and discount/profit(Line no 98-104)
# 11. Monthly sales, profit, and discount trends(Line no 107-114)
# 12. Peak sales months(Line no 117-119)
# 13. Sub-category sales per unit(Line no 121-125)
# 14. Product combinations (market basket)(Line no 128-130)
# 15. Predicting profit using regression(Line no 133-138)


file_path = 'C:/Users/Aai/Downloads/Superstore.csv'
df = pd.read_csv(file_path, encoding='ISO-8859-1')

df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True, errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True, errors='coerce')
df['Delivery Time'] = (df['Ship Date'] - df['Order Date']).dt.days
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month

sns.set(style="whitegrid")

category_profit = df.groupby(['Category', 'Sub-Category'])[['Sales', 'Profit']].sum().reset_index()
print("1. Profit margins by category and sub-category")
print(category_profit)
plt.figure(figsize=(12, 6))
sns.barplot(data=category_profit, x='Sub-Category', y='Profit', hue='Category')
plt.title('Profit by Category and Sub-Category')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

state_profit = df.groupby('State')[['Sales', 'Profit']].sum().reset_index()
print("\n2. Sales and profit by state")
print(state_profit.sort_values(by='Sales', ascending=False).head())
plt.figure(figsize=(12, 6))
top_states = state_profit.sort_values(by='Sales', ascending=False).head(10)
sns.barplot(data=top_states, x='State', y='Sales')
plt.title('Top 10 States by Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

discount_impact = df.groupby('Discount')[['Sales', 'Profit']].mean().reset_index()
print("\n3. Average Sales and Profit by Discount")
print(discount_impact)
plt.figure(figsize=(10, 5))
sns.lineplot(data=discount_impact, x='Discount', y='Profit', label='Profit')
sns.lineplot(data=discount_impact, x='Discount', y='Sales', label='Sales')
plt.title('Impact of Discount on Sales and Profit')
plt.tight_layout()
plt.show()

product_loss = df.groupby('Product Name')[['Sales', 'Profit']].sum().sort_values(by='Profit').head(10).reset_index()
print("\n4. Top 10 Loss-Making Products")
print(product_loss)

delivery_by_mode = df.groupby('Ship Mode')['Delivery Time'].mean().reset_index()
print("\n5. Average Delivery Time by Shipping Mode")
print(delivery_by_mode)
plt.figure(figsize=(8, 5))
sns.barplot(data=delivery_by_mode, x='Ship Mode', y='Delivery Time')
plt.title('Average Delivery Time by Shipping Mode')
plt.tight_layout()
plt.show()

shipmode_profit = df.groupby('Ship Mode')[['Sales', 'Profit']].sum().reset_index()
print("\n6. Profit by Shipping Mode")
print(shipmode_profit)

shipmode_region = df.groupby(['Region', 'Ship Mode'])[['Sales', 'Profit']].sum().reset_index()
print("\n7. Shipping Performance by Region")
print(shipmode_region)

segment_order = df.groupby('Segment').agg({'Sales': 'mean', 'Order ID': 'count'}).reset_index()
print("\n8. Average Order Value by Segment")
print(segment_order)


top_customers = df.groupby(['Customer ID', 'Customer Name'])[['Profit']].sum().sort_values(by='Profit', ascending=False).head(10).reset_index()
print("\n9. Top 10 Profitable Customers")
print(top_customers)

repeat_customers = df.groupby('Customer ID').agg({
    'Order ID': 'nunique',
    'Discount': 'mean',
    'Profit': 'sum'
}).reset_index()
print("\n10. Repeat Customer Behavior")
print(repeat_customers.head())


monthly_trend = df.groupby(['Year', 'Month'])[['Sales', 'Profit', 'Discount']].sum().reset_index()
print("\n11. Monthly Trends in Sales, Profit, and Discount")
print(monthly_trend.head())
plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_trend, x='Month', y='Sales', hue='Year', marker='o')
plt.title('Monthly Sales Trend by Year')
plt.tight_layout()
plt.show()


monthly_peak = monthly_trend.sort_values(by='Sales', ascending=False).head(10)
print("\n12. Peak Sales Months")
print(monthly_peak)

value_per_unit = df.groupby('Sub-Category').agg({'Sales': 'sum', 'Quantity': 'sum'})
value_per_unit['Sales per Unit'] = value_per_unit['Sales'] / value_per_unit['Quantity']
value_per_unit = value_per_unit.reset_index()
print("\n13. Sub-Category Sales per Unit")
print(value_per_unit)


market_basket = df.groupby('Order ID')['Product Name'].apply(lambda x: list(x)).reset_index()
print("\n14. Sample Product Combinations")
print(market_basket.head())


X = df[['Sales', 'Quantity', 'Discount']]
y = df['Profit']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
model = LinearRegression().fit(X_train, y_train)
model_score = model.score(X_test, y_test)
print(f"\n15. Predictive Model R² Score for Profit Estimation: {model_score:.4f}")
