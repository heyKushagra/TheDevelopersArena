#Task 3 of the Internship Project

#Importing the pandas library
import pandas as pd
df = pd.read_csv("sales_data.csv")
print (df)

#Checking missing or null values
#print(df.isnull().sum())

#calculating the total sales
df['Total']=df['Quantity']*df['Price']
total_sales=df['Total'].sum()
print(f"\nTotal Sales: {total_sales}")

#finding best selling product
best_sell=df.groupby('Product')['Quantity'].sum().idxmax()
print(f"Best Selling Product (by quantity): {best_sell}")

#Generating sales report by product with total sales amount
report = df.groupby('Product')['Total'].sum().reset_index()
print("\nSales Report by Product:")
print(report)

#visualizing the data
import matplotlib.pyplot as plt 
plt.bar(report['Product'],report['Total'])
plt.xlabel('Product')
plt.ylabel('Total Sales Amount')
plt.title('Sales Report by Product')
plt.show()
