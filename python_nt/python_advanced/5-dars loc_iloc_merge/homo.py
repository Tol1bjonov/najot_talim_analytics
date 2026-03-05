import pandas as pd

# 1
data = {
    "product_id": [0, 1, 2, 3, 4],
    "low_fats": ["Y", "Y", "N", "Y", "N"],
    "recyclable": ["N", "Y", "Y", "Y", "N"]
}
df = pd.DataFrame(data)

result = df[(df["low_fats"] == "Y") & (df["recyclable"] == "Y")][["product_id"]]
print(result)

# 2
data = {
    "id": [1, 2, 3, 4, 5, 6],
    "name": ["Will", "Jane", "Alex", "Bill", "Zack", "Mark"],
    "referee_id": [ 0, 0,2 , 0 , 1, 2]
}

df = pd.DataFrame(data)
result = df[(df["referee_id"] != 2) | (df["referee_id"].isna())][["name"]]
print(result)

# 3
data = {
    "name": ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola"],
    "continent": ["Asia", "Europe", "Africa", "Europe", "Africa"],
    "area": [652230, 28748, 2381741, 468, 1246700],
    "population": [25500100, 2831741, 37100000, 78115, 20609294],
    "gdp": [20343000000, 12960000000, 188681000000, 3712000000, 100990000000]
}

df = pd.DataFrame(data)
result = df[(df["area"] >= 3000000) | (df["population"] >= 25000000)][["name", "population", "area"]]
print(result)