import pandas as pd
#from pandasql import sqldf
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

file = "Kotelenko/student-mat.csv"#поменять!

df = pd.read_csv(file)

df.info()

print(df.isnull().sum()) #узнаем кол-во Null

#ql = """
#SELECT * 
#FROM df
#"""

#result = sqldf(sql)
#print(result)

#df.drop_duplicates()

#result = sqldf(sql)
#print(result) это сделано чтобы можно было понять, какие столбцы удаленны, так как ответы одинаковые drop_duplicates не нужен 

numeric_data = df.select_dtypes(include=[np.number])

outliers = {}
for col in numeric_data.columns:
    outliers[col] = np.sum(np.abs(numeric_data[col] - np.mean(numeric_data[col])) > 3 * np.std(numeric_data[col]))#мы смотрим по утроенному стандартному отклонению

for col, count in outliers.items():
    print(f"Столбец {col} содержит {count} выбросов.")#считаем вбросы чтобы понимать нужно ли их убирать


for col in numeric_data.columns:
    upper_limit = df[col].mean() + 3 * df[col].std()
    #print(f"{col} upper_limit: {upper_limit}")
    lower_limit = df[col].mean() - 3 * df[col].std()    
    #print(f"{col} lower_limit: {lower_limit}")      
    df = df.loc[(df[col] > lower_limit) & (df[col] < upper_limit)]

df.info()

numeric_data = df.select_dtypes(include=[np.number])
corr_matrix = numeric_data.corr()


sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.show()
