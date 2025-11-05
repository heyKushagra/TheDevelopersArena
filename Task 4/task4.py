#TASK 4: Expense Data Analysis 

import pandas as pd
df=pd.read_csv("expense_data_1.csv")
print(df)

df['Date']=pd.to_datetime(df['Date'])
df['Month']=df['Date'].dt.strftime('%B')

print(df.describe())
print(df['Category'].value_counts())

total_expense=df[df['Income/Expense']=='Expense']['Amount'].sum()
print("Total Expense: ", total_expense)

category_expense=df.groupby('Category')['Amount'].sum().sort_values(ascending=False)
print(category_expense.head())


#Visualizing the data

# Category wise Spending
import matplotlib.pyplot as plt
category_expense.plot(kind='bar', figsize=(8,4))
plt.title('Expenses by Category')
plt.ylabel('Amount (INR)')
plt.xlabel('Category')
plt.show()

# Monthly Spending 
monthly_expense=df.groupby('Month')['Amount'].sum()
monthly_expense.plot(kind='line', marker='o', figsize=(8,4))
plt.title('Monthly Expenses')
plt.ylabel('Amount (INR)')
plt.show()

