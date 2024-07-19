
import egnyte


domain = "apidemo.egnyte.com"
access_token = "f9c7gdmcgc4yq8dz2y95z3sg"


def VerifyCreation():
    client = egnyte.EgnyteClient({"domain": domain, "access_token": access_token})
    #folderPath = "/Shared/Attempt-179"  
    folderPath = "/Shared/"  
    folderList = client.folder(folderPath)
    folderList.list()
    for folder in folderList.folders:
        print(folder)

VerifyCreation()
