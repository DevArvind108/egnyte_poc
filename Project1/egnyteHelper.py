# pip install egnyte ||  Python SDK
# https://developers.egnyte.com/Egnyte_SDK#python
import egnyte

from databaseHelper import UpdateProjectTable


# domain  ="advantage.egnyte.com"
domain = "apidemo.egnyte.com"
access_token = "f9c7gdmcgc4yq8dz2y95z3sg"


#
def VerifyAndCallEgnyteApi(ID, ProjectName, isSku, FolderCreated, SKUs):
    SKUArr = SKUs.split(",")
    # print("FolderCreated %s | Sku %s " % (FolderCreated, SKUs))
    if FolderCreated == False:
        print(
            "API Call With ID :%s, ProjectName :%s , isSku :%s FolderCreated :%s"
            % (ID, ProjectName, isSku, FolderCreated)
        )
        CreateFolderViaEgnyteApi(ID, ProjectName, isSku, SKUArr)
    else:
        print("Skip API Call For %s, ProjectName %s " % (ID, ProjectName))


def CreateFolderViaEgnyteApi(ID, ProjectName, isSku, SKUArr):
    client = egnyte.EgnyteClient({"domain": domain, "access_token": access_token})

    # one time job
    # client.folder("/Shared/main").delete()

    # Create a Project/Main folder
    folderPath = "/Shared/" + ProjectName + "/main"
    generateMainFolder = client.folder(folderPath).create(
        ignore_if_exists=True
    )  # ignore already created.
    print(
        "Input Main Folder Name %s || Generated Path %s : "
        % (folderPath, generateMainFolder.path)
    )
    # Create Link to access the main folder. generateMainFolder
    if generateMainFolder is not None:
        mainLink = CreateFolderLink(
            ID, generateMainFolder.path, "folder", "anyone", False
        )
        print("Main Link %s : " % (mainLink[0].url))
        UpdateProjectTable(ID, mainLink[0].url, False)

    subFolderLinkCSV = ""
    # Create SubFolder if Sku Exists.
    if isSku is True and len(SKUArr) > 0:
        print("=======================================================Sub Folder Links=======================================================")
        for sku in SKUArr:
            subfolder = client.folder(folderPath + "/" + sku).create(
                ignore_if_exists=True
            )
            print(
                "Input SubFolder Folder Name : %r || Generated SubFolder Path : %r "
                % (sku, subfolder.path)
            )
            # Create Link to access the folder.
            subLink = CreateFolderLink(ID, subfolder.path, "folder", "anyone", True)
            print("SKU Link %s : " % (subLink[0].url))
            subFolderLinkCSV += subLink[0].url + " ### "

        print("=======================================================Sub Folder Links=======================================================")
        
    if len(subFolderLinkCSV) > 0:
        UpdateProjectTable(ID, subFolderLinkCSV, True)

        # save to db for ID

    # else:
    #     print("No SKU")


def CreateFolderLink(ID, folderPath, type, accessibility, isSubFolder):
    #print("Crating link")
    client = egnyte.EgnyteClient({"domain": domain, "access_token": access_token})
    link = client.links.create(folderPath, type, accessibility)
    #print("Input Folder For Link %s || Generated Link %s : " % (folderPath, link[0].url))
    return link


def VerifyCreation(ProjectName):
    client = egnyte.EgnyteClient({"domain": domain, "access_token": access_token})
    folderPath = "/Shared/" + ProjectName
    folderList = client.folder(folderPath)
    folderList.list()
    for folder in folderList.folders:
        print(folder)


# client.links.create(
#     "",
# )
