import pandas as pd
#from pandasql import sqldf
import numpy as np


file = "Kotelenko/student-mat.csv"#поменять!

df = pd.read_csv(file)

df.info()

print(df.isnull().sum())

sql = """
SELECT * 
FROM df
"""

#result = sqldf(sql)
#print(result)

#df.drop_duplicates()

#result = sqldf(sql)
#print(result) это сделано чтобы можно было понять, какие столбцы удаленны, так как ответы одинаковые drop_duplicates не нужен 

numeric_data = df.select_dtypes(include=[np.number])

outliers = {}
for col in numeric_data.columns:
    outliers[col] = np.sum(np.abs(numeric_data[col] - np.mean(numeric_data[col])) > 3 * np.std(numeric_data[col]))

percent_outliers = {}
for col in numeric_data.columns:
    percent_outliers[col] = (outliers[col] / numeric_data[col].shape[0]) * 100


for col, percent in percent_outliers.items():
    percent = percent/100
    q_low = df[col].quantile(percent)
    print(q_low)
    q_high = df[col].quantile(0.95)
    print(q_high)    
