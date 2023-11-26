import pandas as pd
#from pandasql import sqldf
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objs as go

file = "Kotelenko/student-mat.csv"#поменять!

df = pd.read_csv(file)

df.info()

print(df.isnull().sum()) #узнаем кол-во Null, так как нету , ничего делать с этим не будем


df = df.drop_duplicates()

df.info() 

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

df = df.replace({'yes': 1, 'no': 0})

numeric_data = df.select_dtypes(include=[np.number])
corr_matrix = numeric_data.corr()


sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", annot_kws={"fontsize": "x-small"})

plt.show()


x = (df["G2"])
y = (df["G3"])
z = (df["failures"])


fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers', marker=dict(color=z, size=10))])

fig.update_layout(scene=dict(xaxis_title="G2", yaxis_title="G3", zaxis_title="failures"))

fig.show()

x = (df["G3"])
y = (df["G2"])
z = (df["G1"])

fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers', marker=dict(color=z, size=10))])

fig.update_layout(scene=dict(xaxis_title="G3", yaxis_title="G2", zaxis_title="G1"))

fig.show()


