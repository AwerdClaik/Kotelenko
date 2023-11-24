import pandas as pd
from pandasql import sqldf

file = "student-mat.csv"

df = pd.read_csv(file)

df.info()

sql = """
SELECT * 
FROM df
"""

#result = sqldf(sql)
#print(result)

#df.drop_duplicates()

#result = sqldf(sql)
#print(result) это сделано чтобы можно было понять, какие столбцы удаленны, так как ответы одинаковые drop_duplicates не нужен 

