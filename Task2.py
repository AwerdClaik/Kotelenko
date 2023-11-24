import pandas as pd
#from pandasql import sqldf

file = "Kotelenko\student-mat.csv"#поменять!

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

for var in int_cols:
    q_low = df[int_cols].quantile(0.05)
    print(q_low)
    q_high = df[int_cols].quantile(0.95)
    print(q_high)    
    data = data.loc[(data["var1"] > q_low) & (data["var1"] < q_high)]    
    

