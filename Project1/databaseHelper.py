# Install the Microsoft ODBC Driver 18 for SQL Server
# pip install pyodbc | Successfully installed pyodbc-5.1.0
# pip list
# pyodbc package from PyPI.

import pyodbc

# from databaseHelper


connectionString = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER=localhost;DATABASE=Testo;UID=sa;PWD=1234"
conn = pyodbc.connect(connectionString)
SQL_QUERY_MAIN = "UPDATE [dbo].[tblProject] SET [MainFolderLink] = 'XX' , [FolderCreated] =1 WHERE [ID] ='YY'"
SQL_QUERY_SUB = "UPDATE [dbo].[tblProject] SET [SKUFoldersLink] = 'XX' , [FolderCreated] =1  WHERE [ID] ='YY'"


def UpdateProjectTable(ID, link, isSubfolder):
    cursor = conn.cursor()
    query = "CCCCC"
    if isSubfolder is True:
        query = SQL_QUERY_SUB.replace("XX", link)
        query= query.replace("YY",str(ID))
    else:
        query = SQL_QUERY_MAIN.replace("XX", link)
        query= query.replace("YY",str(ID))
    

    cursor.execute(query)
    cursor.commit()
