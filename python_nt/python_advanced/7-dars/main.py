import pandas as pd


df = pd.DataFrame({
    'employee': ['Ali','Vali','Sami','Lola','Sara','John','Mike'],
    'department': ['IT','IT','HR','HR','HR','IT','HR'],
    'salary': [1000,1500,800,900,1200,1100,900],
    'date': pd.to_datetime([
        '2024-01-01','2024-01-02','2024-01-01',
        '2024-01-02','2024-01-03','2024-01-03','2024-01-04'
    ])
})


##           OFFSET functions
# lag whole table
df['lag_salary'] = df['salary'].shift(1) # pastga tushiradi

df['lag_salary'] = df['salary'].shift(-1)  #tepaga tushiradi

# lag each department
df.sort_values(['department', 'date'], inplace=True)

df['lag_salary_dep'] = df.groupby('department')['salary'].shift(1)

# CUMULATIVE FUNCTIONS
# running total whole table
df.sort_values('date', inplace=True)
df['cum_total'] = df['salary'].cumsum()

# running total each department
df.sort_values(['department','date'], inplace=True)
df['cum_total'] = df.groupby('department')['salary'].cumsum()

# har bitta department boyicha hozirgi va oldingi kunning farqini va 
# uning running totalini hisoblaymiz

df.sort_values(['department', 'date'], inplace=True)
df['lead_salary'] = df.groupby('department')['salary'].shift(1)
df['difference'] = df['salary'] - df['lead_salary']
df['run_tot'] = df['difference'].cumsum()
df

## ROLLING
# har nechtasida nima qilishni aytadi
df['rolling_sum'] = df['salary'].rolling(2).sum()
df


### New DF for classwork
df = pd.DataFrame({
    'employee': ['Ali','Vali','Sami','Lola','Sara','John','Mike','Anna','Tom','Zara'],
    'department': ['IT','IT','HR','HR','HR','IT','HR','IT','HR','IT'],
    'date': pd.to_datetime([
        '2024-01-01','2024-01-03','2024-01-01','2024-01-02','2024-01-03',
        '2024-01-04','2024-01-04','2024-01-05','2024-01-05','2024-01-06'
    ]),
    'sales': [200,350,150,180,220,400,210,300,190,500]
})

# 1
df.sort_values('department', inplace=True)
df['avg_sales'] = df.groupby('department')['sales'].transform('mean')

# 2 har bir xodimning department ichidagi ranki, katta qiymat 1
df['ranking_sales'] = df.groupby('department')['sales'].rank(ascending=False)
df.sort_values(['department', 'ranking'], inplace=True)
df

# 3 har bir department ichida row_number date boyicha
df['ranking_date'] = df.groupby('department')['date'].rank(ascending=False)
df

# 4 har bir department ichida kngi kun savdosi lead
df.sort_values('department', inplace=True)
df['next_day'] = df.groupby('department')['sales'].shift(1)
df

# 5 har bir department boyicha cummulative sales, date boyicha
df.sort_values(['department','date'] , inplace=True)
df['cum_total'] = df.groupby('department')['sales'].cumsum()
df

# 6 har bir department ichida 3 kunlik moving avg 
df.sort_values('department', inplace=True)
df['rolling_avg'] = df.groupby('department')['sales'].rolling(3).mean().reset_index(level=0, drop=True)
df

# 9 har bir department ichida eng yuqori 2 ta saleschi xodim
df.sort_values('department', inplace=True)
df.groupby('department')['sales'].max()['employee']
