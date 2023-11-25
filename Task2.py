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

for col in numeric_data.columns:
    upper_limit = df[col].mean() + 3 * df[col].std()
    print(f"{col} {upper_limit}")
    lower_limit = df[col].mean() - 3 * df[col].std()    
    print(f"{col} {lower_limit}")      
