import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import random

df = pd.read_csv('student-mat.csv')

df.info()

print(df.isnull().sum()) #узнаем кол-во Null, так как нету , ничего делать с этим не будем

df = df.drop_duplicates()

df.info()
#Видим что в df не было дубликатов

numeric_data = df.select_dtypes(include=[np.number])

outliers = {}
for col in numeric_data.columns:
    outliers[col] = np.sum(np.abs(numeric_data[col] - np.mean(numeric_data[col])) > 3 * np.std(numeric_data[col]))

for col, count in outliers.items():
    print(f"Столбец {col} содержит {count} выбросов.")
#считаем вбросы чтобы понимать нужно ли их убирать

for col in numeric_data.columns:
    upper_limit = df[col].mean() + 3 * df[col].std()
    #print(f"{col} upper_limit: {upper_limit}")
    lower_limit = df[col].mean() - 3 * df[col].std()
    #print(f"{col} lower_limit: {lower_limit}")
    df = df.loc[(df[col] > lower_limit) & (df[col] < upper_limit)]

df.info()
#Убираем выбросы и смотрим сколько данных осталось

print(df.head())

"""plt.figure(figsize=(13,8))
plt.boxplot(numeric_data.values)
plt.xticks(range(1, len(numeric_data.columns) + 1), numeric_data.columns)
#plt.show()#ещё бы убрать потом из графика ненужное"""

for col in numeric_data:
  plt.boxplot(df[col])
  plt.xlabel(col)
  plt.title(col)
  #plt.show()
#получи представления с какими данными мы будем работать

object_data = df.select_dtypes(include=[object])
print(object_data)

for col in object_data.columns:
  counter = df.groupby(col)[col].count()
  plt.bar(counter.index, counter.values, color = (random.random(), random.random(), random.random()))
  plt.xlabel(col)
  plt.ylabel('Количество')
   #plt.show()

#так как далее мы будем работать с int столбцами , изучим распределение значений в str столбцах

score_list = ["G1", "G2", "G3"]
cols_to_plot = object_data.columns

melted_df = pd.melt(df, id_vars=cols_to_plot, value_vars=score_list, var_name="period grade")

for col in cols_to_plot:
    sns.boxplot(x=col, y="value", hue="period grade", data=melted_df)
    plt.ylabel("score")
    plt.title(col)
    #plt.show()
#и посмотрим различные факторы типа str на влияние оценки
#Каждый график подсвечивает интересные моменты , например , что идеальная работа отца это учитель , а матери врачем, что доступ в интернет улучшает оценки , а наличие отношений , вредит

df = df.replace({'yes': 1, 'no': 0})
#проанализировав смысл столбцов , можем заменить yes на 1 а no на 0 , чтобы увеличить кол-во парамметров , которые влияют на успеваемость


numeric_data = df.select_dtypes(include=[np.number])
corr_matrix = numeric_data.corr()

plt.figure(figsize=(13,8))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", annot_kws={"fontsize": "x-small"})
#plt.show()
#инетересное наблюдение, это то что люди , которыу пьют алкоголь мало уделают времни учебе , но это не коррелирует с оценками 

x = (df["G2"])
y = (df["G3"])
z = (df["failures"])


fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers', marker=dict(color=z, size=10))])

fig.update_layout(scene=dict(xaxis_title="G2", yaxis_title="G3", zaxis_title="failures"))

fig.show()
#мы видим кол-во прошлых провалов в классе влияют на успеваемость, так как у отлиников их нету,  как мы видим есть исключения, но всё равно это не отличники
#Кроме того видно небольшую тендецию снижения оценок в зависимости от  кол-во прошлых провалов в классе

x = (df["G3"])
y = (df["G2"])
z = (df["G1"])

fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers', marker=dict(color=z, size=10))])

fig.update_layout(scene=dict(xaxis_title="G3", yaxis_title="G2", zaxis_title="G1"))

fig.show()

#мы видим максимальную кореляцию прошлых оценок и будующих


