# -*- coding: utf-8 -*-
"""
Created on Thu May 30 16:21:54 2019

@author: Intern
"""



import pyodbc 
import pandas as pd

server = "imccodes.database.windows.net,1433"
username = "ICDCPT"
password = "IMCcodes!18q4"
database = "imccodes"
#myDriver = "{SQL Server}"
# OR "ODBC Driver 17 for SQL Server"?


conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

sql = 'select * from D2'
sql2 = 'select * from D6'

ICDcodes = pd.read_sql(sql,conn)
Pcodes = pd.read_sql(sql2,conn)

conn.close()

ICDcodes=ICDcodes.drop(columns='rownames')
Pcodes=Pcodes.drop(columns='rownames')

#change index








'''cursor = conn.cursor() 



cursor.execute('SELECT * FROM D2')
ICDcodes=cursor.fetchall()

cursor.execute('SELECT * FROM D6')
Pcode=cursor.fetchall()
    
conn.close()



ICD=open('ICDtrial.txt','w')
for item in ICDcodes:
    print(item,file=ICD)
ICD.close()


Pcodes=open('Pcodestrial.txt','w')
for item in Pcode:
    print(item,file=Pcodes)
ICD.close()
'''






