# Install the Microsoft ODBC Driver 18 for SQL Server
# pip install pyodbc | Successfully installed pyodbc-5.1.0
# pip list
# pyodbc package from PyPI.
# to run & C:/Users/arryn/AppData/Local/Microsoft/WindowsApps/python3.11.exe c:/MyDrive/Git2/egnyte_poc/Proejct1/main.py
#trouble shoot vscode C+S+P select interpreter =>C:/Users/arryn/AppData/Local/Microsoft/WindowsApps/python3.11.exe

import pyodbc

from egnyteHelper import VerifyAndCallEgnyteApi, VerifyCreation


connectionString = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER=localhost;DATABASE=Testo;UID=sa;PWD=1234"
conn = pyodbc.connect(connectionString)
SQL_QUERY = "SELECT [ID],[ProejctName],[isSku],[FolderCreated],[SKUs] FROM [dbo].[tblProject] where [FolderCreated] = 0"

cursor = conn.cursor()
cursor.execute(SQL_QUERY)

ID = 0
ProjectName = ""
isSku = ""
FolderCreated = ""
SkuCSV = ""


for row in cursor:
    if len(row) == 5:
        ID = row[0]
        ProjectName = row[1]
        isSku = row[2]
        FolderCreated = row[3]
        SkuCSV = row[4]
        #print(row)
        print("__________________________________________________________________________________________________________________________________________________")
        print('ID : %r | Project Name : <%r> | SKU : <%r> | Created : %r'  % (ID ,  ProjectName, SkuCSV, FolderCreated))
        # print('isSku = %r' % isSku)
        # print('FolderCreated = %r' % FolderCreated)
        # print('SKU = %r' % SkuCSV)

        # //Call Asana Api
        #print("Verifying Project Data and Calling Egnyte Apis")
        VerifyAndCallEgnyteApi(ID, ProjectName, isSku, FolderCreated, SkuCSV)
    else:
        print("Skip")


# verify creation
    #VerifyCreation()
