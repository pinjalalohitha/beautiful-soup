import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('sales_data.csv')
print("First 5 rows of the dataset:")
print(df.head())
df_region = df[df['Region'] == 'East']
print("\nFirst 5 rows of the dataset for the 'East' region:")
print(df_region.head())
df_sorted = df.sort_values(by='Date', ascending=True)
print("\nFirst 5 rows of the dataset sorted by 'Date':")
print(df_sorted.head())
df_grouped = df.groupby('Region')['Sales'].sum().reset_index()
print("\nTotal sales by region:")
print(df_grouped)
mean_sales = df.groupby('Region')['Sales'].mean().reset_index()
print("\nMean sales by region:")
print(mean_sales)
mean_sales_value = df['Sales'].mean()
median_sales_value = df['Sales'].median()
std_sales_value = df['Sales'].std()
print(f"\nMean Sales: {mean_sales_value:.2f}")
print(f"Median Sales: {median_sales_value:.2f}")
print(f"Standard Deviation Sales: {std_sales_value:.2f}")
plt.figure(figsize=(10, 6))
plt.hist(df['Sales'], bins=50, edgecolor='k')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.title('Sales Distribution')
plt.grid(True)
plt.show()
plt.figure(figsize=(10, 6))
sns.set(style="whitegrid")
sns.barplot(x='Region', y='Sales', data=df_grouped)
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.title('Total Sales by Region')
plt.show()

