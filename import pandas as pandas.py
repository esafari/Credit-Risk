import pandas as pandas
import pyodbc
import pandas as pd

conn = pyodbc.connect('DRIVER={SQL Server};'
                      'SERVER=UOFL23-PF1RTRQ6;'
                      'DATABASE=TSQL2012;')
query = "SELECT * FROM sales.Orders ;"
df = pd.read_sql(query, conn)
print(df.shape)
