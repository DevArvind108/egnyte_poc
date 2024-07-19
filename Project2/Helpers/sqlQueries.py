from enum import Enum


class Query(Enum):
    Project = """SELECT p.[PID]
      ,p.[PortfolioID]
      ,p.[PortfolioName]
      ,p.[ProjectID]
      ,p.[ProjectName]
      ,p.[IsEgnyteFolderCreated]
      ,p.[IsEgnyteFolderCreatedOn]  FROM [dbo].[AsanaProjectTb] as p Where p.IsActive = 1 and p.IsEgnyteFolderCreated = 0 """
    SKU = """SELECT p.[SkuID]
      ,p.[PID]
      ,p.[SKUFolderTitle]
      ,p.[IsEgnyteFolderCreated]
      ,p.[IsEgnyteFolderCreatedOn]  FROM [dbo].[AsanaProjectSKUTb] as p Where p.IsActive = 1 and p.IsEgnyteFolderCreated = 0"""


# print(Query.project)
# print(Query.SKU.name)
