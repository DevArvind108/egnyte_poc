# pip install egnyte ||  Python SDK
#https://developers.egnyte.com/Egnyte_SDK#python
import egnyte
#domain  ="advantage.egnyte.com"
domain  ="apidemo.egnyte.com"
access_token  = "f9c7gdmcgc4yq8dz2y95z3sg" 




def VerifyAndCallEgnyteApi(ID,ProjectName,isSku,FolderCreated,Skus):
  if FolderCreated == False :
    print("API Call With ID % s, ProjectName % s , isSku % s FolderCreated % s" % (ID,ProjectName,isSku,FolderCreated));
    CallEgnyteApi(ID,ProjectName,isSku,Skus)
  else:  
    print("Skip API Call For % s, ProjectName % s " % (ID,ProjectName))

def CallEgnyteApi(ID,ProjectName,isSku,Skus):
  client = egnyte.EgnyteClient({"domain":domain , "access_token" :access_token})
  
  #one time job 
  #client.folder("/Shared/main").delete()
  
  client.links.create('',)
  # Create a folder
  folderPath ="/Shared/"+ProjectName +"/main"
  print("--------------------")
  print(folderPath)
  folder = client.folder(folderPath).create(ignore_if_exists=True)
  print("Create a folder")
  print(folder)
  if isSku is True :
      for sku in Skus:
          subfolder = client.folder(folderPath+"/"+sku).create(ignore_if_exists=True)
          print ("SubFolder Created % s ::" % subfolder)
  else:
     print("No SKU")
     
     
def VerifyCreation():
  client = egnyte.EgnyteClient({"domain":domain , "access_token" :access_token})
  folderList = client.folder("/Shared/")
  folderList.list()
  for folder in folderList.folders:
    print(folder)
    
  
  
     
      
      
   