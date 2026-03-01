import pandas as pd 

# data = {
#     "Name": ["Ali", "Vali", "Sami", "Lola"],
#     "Age": [23, 30, 27, 22],
#     "Salary": [500, 800, 600, 450],
#     "City": ["Tashkent", "Samarkand", "Bukhara", "Tashkent"]
# }

# df = pd.DataFrame(data)  # DataFrame da F katta

# # LOC -  qator index va ustun nomi
# # df.loc(qator_index, ustun_nomi)

# # index 
# df.loc[[1]]
# df[1:3]

# # ustun
# df.loc[2, 'Age']
# df.loc[0, 'Salary']

# # shart bilan filter qilish
# df.loc[(df['Age']>25) & (df['Salary']>500), 'Name']
# df.loc[df['City'] == 'Tashkent', ['Name', 'Salary']]

# # qiymatni ozgartirish
# df.loc[2,'Age'] = 50
# df.loc[df['Age']>25, 'Salary'] = df['Salary'] * 1.1

# df.loc[[0,2,3], ['Name', 'Age']]

# # 1-usul
# a=[]
# for i in range(0,100):
#     a.append(i)

# df.loc[df.index % 2 ==0, ['Name', 'Age']]

# # ILOC
# df.iloc[1:3, 0:2]

# # MERGE
# import pandas as pd

# df_customers = pd.DataFrame({
#     'customer_id': [1, 2, 3, 4],
#     'name': ['Ali', 'Vali', 'Gulnoza', 'Diyor']
# })

# df_orders = pd.DataFrame({
#     'order_id': [101, 102, 103, 104, 105],
#     'customer_id': [1, 2, 2, 5, 6],
#     'amount': [250, 150, 200, 300, 500]
# })

# # INNER JOIN
# inner_join = pd.merge(df_customers, df_orders, on='customer_id', how='inner')

# # LEFT JOIN
# left_join = pd.merge(df_customers, df_orders, on='customer_id', how='left')

# # RIGHT JOIN
# right_join = pd.merge(df_customers, df_orders, on='customer_id', how='right')

# # OUTER JOIN
# outer_join = pd.merge(df_customers, df_orders, on='customer_id', how='outer')

# print("Inner Join:\n", inner_join)
# print("Left Join:\n", left_join)
# print("Right Join:\n", right_join)
# print("Outer Join:\n", outer_join)









# Classwork
clubs = pd.read_csv('clubs.csv')
leagues = pd.read_csv('leagues.csv')
matches = pd.read_csv('matches.csv')
players = pd.read_csv('players.csv')

# 1
leagues[['league_name', 'founded_year']]
# 2
leagues.loc[[1], ['total_teams']]

club_leagues = pd.merge(clubs, leagues, on='league_id', how='inner')
                    # 1-yoli
all = club_leagues.groupby('league_name', as_index=False).agg({'club_name': 'count'})
all[all['league_name'] == 'Premier League']
                    # 2-yoli
all = club_leagues.groupby('league_name').agg({'club_name': 'count'})
all.loc[all.index == 'Premier League']

# 3
f_year = clubs[clubs['founded_year'] > 2000]

# 4
club_players = pd.merge(players, clubs, on='club_id', how='left')
club_players[['player_name', 'club_name', 'age']]

# 5
clubs[clubs['club_name']=='FC Barcelona']

# 6
players[players['salary_monthly']>400]

# 7
players.loc[players['nationality'].isin(['Portugal', 'Brazil']), ['player_name']]

# 8
players[players['age']>30]