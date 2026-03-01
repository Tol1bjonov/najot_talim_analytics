 # %%
import pandas as pd

# # Series
s = pd.Series([1,2,3,4,5])
s[3]
s[4] = 100
s

# Index
s=pd.Series([1,2,3,4], index=['a', 'b', 'c', 'd'])
s['b']
s['b':'d']
s.index
s.values

# Arifmetik amallar
s=pd.Series([1,2,3,4])
s1 = pd.Series([5,0,10, 50])
s+s1
s*2

# Statistiks operations
s=pd.Series([1,2,3,4,5,6,7])
s.sum()
s.median()
s.count()
s.describe()


# Filtering

s = pd.Series([1,2,3,4,5,6])
s[s>3]
s[s%2==0]
s[s>3] = 100 

#  Add values
a=pd.Series([1,2,3,4])
print(a)
a[5] = 100

x = [1,2,3,4,5,5,6,7]
x1 = pd.Series(x)

result = pd.concat([a, x1])

# puzzle 1
s = pd.Series([5,10, 20, 40])
s*2
s[s>10] = 100

# puzzle 2
s1 = pd.Series([3,8,12,5,20])
s1[s1%2==0] = 0
s1[s1%2!=0] = 1
s1

# puzzle 3
s2 = pd.Series([5,12,18,7,25,30,3,15, 10])
s2[s2<10] = 0
s2[(s2 > 10) & (s2 < 20)] = 1
s2[s2>20] = 2
s2

# puzzle 4
s3 = pd.Series([100,200,150,80,50])
s3 = s3 - (s3*0.1) * (s3>100)
s3 = s3 - (s3*0.05) * (s3<100)
s3



### Dataframe
import pandas as pd

data = {
    'name': ['Ali', 'Vali', 'Hasan'],  
    'age' : [23, 34, 45],            
    'salary' : [1200, 1400, 1600]
}

df = pd.DataFrame(data)
df

data1 = [
    ['ali', 23, 2300],
    ['vali', 25, 3000],
    ['hasan', 45, 5000]
]
df1 = pd.DataFrame(data1, columns=['name', 'age', 'salary'], index=['a', 'b', 'c'])
df1


df1['country'] = ['tashkent', 'andijan', 'samarkand']
df1

## Delete
df1.drop('country', axis=1, inplace=True)
df1


# %%


