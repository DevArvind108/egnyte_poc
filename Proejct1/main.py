# Install the Microsoft ODBC Driver 18 for SQL Server
# pip install pyodbc | Successfully installed pyodbc-5.1.0
# pip list
# pyodbc package from PyPI.
import pyodbc

from egnyteHelper import VerifyAndCallEgnyteApi, VerifyCreation


connectionString = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER=localhost;DATABASE=Testo;UID=sa;PWD=1234"
conn = pyodbc.connect(connectionString) 
SQL_QUERY = "SELECT [ID],[ProejctName],[isSku],[FolderCreated] FROM [dbo].[tblProject] where [FolderCreated] = 0"

cursor = conn.cursor()
cursor.execute(SQL_QUERY)

ID =0
ProjectName =''
isSku=''
FolderCreated =''
Skus = ["Ford1", "Volvo1", "BMW1"]

for row in cursor:
    if(len(row) == 4) :
        ID = row[0]  
        ProjectName =row[1]
        isSku = row[2]
        FolderCreated = row[3]
        # print('ID = %r' % ID)
        #print('ProjectName = %r' % ProjectName)
        # print('isSku = %r' % isSku)
        # print('FolderCreated = %r' % FolderCreated)
       
        #//Call Asana Api
        print('Verifying Project Data')
        VerifyAndCallEgnyteApi(ID,ProjectName,isSku,FolderCreated, Skus)

    else :
        print('Skip')
        

#verify creation
VerifyCreation()
