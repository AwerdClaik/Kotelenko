import pandas as pd
from pandasql import sqldf

file = "student-mat.csv"

df = pd.read_csv(file)


query = """
SELECT *
FROM df
"""

result = sqldf(query)
print(result)

