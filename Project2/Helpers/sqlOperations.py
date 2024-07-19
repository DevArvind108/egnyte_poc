# Example usage:
from .sqlServerHelper import SQLServerHelper

server_name = "localhost" #appsettings/
database_name = "Testo"
username = "sa"
password = "1234"

#store api username pass : key vault
#daymonidtoExclude: + sql connection in enviornemtn process.env.AZURE_SQL_AUTHENTICATIONTYPE;

class SqlOperations:
    # def __init__(self):
    #     _self = self

    def getRowsFromTable(query):
        sql_helper = SQLServerHelper(server_name, database_name, username, password)
        sql_helper.connect()

        # Example query execution
        # query = "SELECT * FROM your_table"
        rows = sql_helper.execute_query(query)
        # if rows:
        #     for row in rows:
        #         print(row)
        
        sql_helper.disconnect()
        return rows
