# main.py


from Helpers.sqlOperations import SqlOperations
from Helpers.sqlQueries import Query
from Helpers.genericHelpers import printRows


projectRows = SqlOperations.getRowsFromTable(Query.Project.value)
printRows(projectRows)

skuRows = SqlOperations.getRowsFromTable(Query.SKU.value)
printRows(skuRows)
