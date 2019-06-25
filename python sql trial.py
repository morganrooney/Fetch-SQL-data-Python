# -*- coding: utf-8 -*-
"""
Created on Thu May 30 16:21:54 2019

@author: Intern
"""



import pyodbc 


server = "imccodes.database.windows.net,1433"
username = "ICDCPT"
password = "IMCcodes!18q4"
database = "imccodes"
#myDriver = "{SQL Server}"
# OR "ODBC Driver 17 for SQL Server"?


conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)


cursor = conn.cursor() 

ICD=cursor.execute('SELECT * FROM D2')

Pcodes=cursor.execute('SELECT * FROM D6')

ICD10=[]
for row in ICD:
    ICD10.append(row)
ICD10

for row in Pcodes:
    print(row)
    
conn.close()
