#%%
import pandas as pd
# df = pd.read_csv('Walmart_Sales.csv')
# df

# kerakli ustunlar
# df = pd.read_csv('Walmart_Sales.csv', usecols=['Store', 'Date', 'Temperature', 'Weekly_Sales'])
# n qatorni chiqarish
# df = pd.read_csv('Walmart_Sales.csv', nrows = 20)
# df

# # # header
# df = pd.read_csv('Walmart_Sales.csv', nrows = 20, header=3)
# df

# # # tekshirish
# df.head(10)
# df.tail(2)
# df.describe()
# df.columns
# df.dtypes

# # # ustun va qatorlar bilan ishlash
# df[['Date']]

# # Filtering
# df[df['Temperature']>50]
# df[(df['Temperature']>50) & df['Date'] == '03-02-2012']
# df[(df['Temperature'] > 50) | (df['Date'] == '03-02-2012')]

# # sanasi 19-02-2010 yoki 26-03-2010 bolgan weekly_sales 1900000 va 2000000 orasida bolgan qatorlar
# df[ 
#     ((df['Date'] == '19-02-2010') | (df['Date'] == '26-03-2010')) 
#     & 
#     (df['Weekly_Sales'].between(1900000, 2000000))
# ] 

# df[((df['Date'] == '19-02-2010') | (df['Date'] == '26-03-2010')) & (df['Weekly_Sales'].between(1900000, 2000000))]

# # Missing Values
# df['Weekly_Sales'].isnull()
# df[df['Weekly_Sales'].isnull()]
# df['Weekly_Sales'].fillna('Qiymat yoq')
# # null qatorlarni drop qilish
# df["Weekly_Sales"].dropna()

# # Saralash va tartiblash
# df.sort_values(by='Temperature')  #asc
# df.sort_values(by='Temperature', ascending=False)  #desc
# df.sort_index
# df.sort_index(ascending=False)

# # Group by
# df.groupby('Date')['Weekly_Sales'].sum()  # bu series
# df.groupby('Date', as_index=False)['Weekly_Sales'].sum().sort_values('Weekly_Sales', ascending=False)

# df.groupby('Date', as_index=False).agg({'Weekly_Sales': 'mean', "Temperature": 'max'}).rename(columns={'Weekly_Sales': 'Total_Sales', 'Temperature': 'MaxTemp'})

# result = df.groupby('Date', as_index=False).agg({'Weekly_Sales': 'sum', 'Fuel_Price': 'max', 'CPI': 'min', 'Temperature': 'mean', }).rename(columns={'Weekly_Sales': 'Total_Sales', 'Fuel_Price': 'Fuel_P_max', 'CPI':'CPI_min', 'Temperature': 'Temperature_avg'}).sort_values(by='Date', ascending=False)
# faylga yuklash
# result.to_csv('result.csv', index=False)



### Amazon ###
#1 top 2 ta kategoriya
df2 = pd.read_csv('Amazon.csv')
df2
most_categories = df2.groupby('Category', as_index=False).agg({'SKU': 'sum'}).head(2)
most_categories.to_csv('amazon_top_category.csv', index=False)

#2 har bir kun uchun sotilgan mahsulot miqdori
daily_sales = df2.groupby('Date', as_index=False).agg({'SKU': 'count'})
daily_sales

#3 currency berilmagan qatorlar
df2[df2['currency'].isnull()]

#4 top 5 ta ship city, amount boyicha
result = df2.groupby('ship-city', as_index=False).agg({'Amount': 'sum'}).head(5)
result

#5 ‘05-31-22’ kuni nechta buyurtma bo‘lgan
df
