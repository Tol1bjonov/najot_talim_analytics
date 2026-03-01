import pandas as pd

df = pd.read_csv('Amazon.csv')
df
#1 top 2 ta kategoriya
most_categories = df.groupby('Category', as_index=False).agg(total_orders=('Order ID', 'count')).sort_values('total_orders', ascending=False).head(2)
most_categories
most_categories.to_csv('amazon_top_category.csv', index=False)

#2 har bir kun uchun sotilgan mahsulot miqdori
daily_sales = df.groupby('Date', as_index=False).agg(total_sales=('Order ID', 'count'))
daily_sales

#3 currency berilmagan qatorlar
df[df['currency'].isna()]

#4 Top 5 ta ship-city amount bo’yicha
result = df.groupby('ship-city', as_index=False).agg(total_amount=('Amount', 'sum')).sort_values('total_amount', ascending=False).head(5)
result

#5 ‘05-31-22’ kuni nechta buyurtma bo‘lgan
orders = df[df['Date'] == '05-31-22']['Order ID'].count()
orders

#6 ship-state va date bo’yicha guruhlab total_quantity va total_amount ni hisoblang yangi filega yozing
result = df.groupby(['ship-state', 'Date'], as_index=False).agg({'Amount': 'sum'}).rename(columns={'Amount':'Total_amount'})
result.to_csv('total_amount.csv', index=False)

#7 B2B true bo’lganlari ichidan har bitta category bo’yicha avg_quantity va avg_amount ni topasiz
filtered = df[df['B2B'] == True]
result = filtered.groupby('Category', as_index=False).agg({'Amount': 'mean'}).rename(columns={'Amount':'avg_amount'})
result

#8 Har bir category bo’yicha umumiy miqdorni topasiz va 1000 dan yuqori bo’lganlarini alohida filega saqlaysiz.
filtered = df.groupby('Category', as_index=False).agg({'Amount' : 'sum'})
filtered[filtered['Amount'] > 1000].to_csv('over_1000.csv', index=False)