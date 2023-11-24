import pandas as pd
from pandasql import sqldf

file = "student-mat.csv"

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

int_cols = [col for col in df.columns if df.dtypes[col] == 'int64']
print(int_cols)

q_low = df["var1"].quantile(0.05)
q_high = df["var1"].quantile(0.95)


