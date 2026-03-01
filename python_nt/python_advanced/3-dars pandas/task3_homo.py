# %%
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name" : ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim'],
    "Age" : [25, 30, 28, 35, 40],
    "Salary": [3000, 4500, 4000, 5000, 6000]
})
df

#### 1-vazifa ###
# ortacha yosh
avg_age = sum(df['Age']) / len(df['Age'])
avg_age
# eng katta maosh
max_salary = max(df['Salary'])
max_salary
# yangi bonus ustuni
df['Bonus'] = df['Salary'] * 0.1
df


### 2-vazifa ###
# df_age = df[df['Age']>30]
# df_age
# df_salary = df[df['Salary']<=4000]
# df_salary
# df.drop('Salary', axis=1, inplace=True)
# df


### 3-vazifa ###
# numpy bilan
# df['Level'] = np.where(df['Age']>=30, 'Senior', 'Junior')
# df
## manual qolda
# df_senior = df[df['Age']>30]
# df_senior['Level'] = 'Senior'
# df_junior = df[df['Age']<30]
# df_junior['Level'] = 'Junior'
# df_final = pd.concat([df_senior, df_junior])
# df_final
## lambda bilan
# df['Level'] = df['Age'].map(lambda x: 'Senior' if x>30 else 'Junior')
# df
# df.columns

### 4-vazifa ###
# df[df["Salary"] == df["Salary"].max()]

### 5-vazifa ###
# df[df["Age"] > sum(df['Age']) / len(df['Age'])]

### 6-vazifa ###
# df['Salary'] = df['Salary'] * (1.2 *(df['Age']<30) + 1*(df['Age']>=30))
# df
df['Salary'] = df.apply(lambda x: x['Salary']*1.2 if x['Age'] <30 else x['Salary'], axis=1)
df
