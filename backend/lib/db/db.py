from lib.utils.cryptic import hash_string
from lib.utils.actions import generate_alphanumeric_code

def register_user(username, password):
    if check_username_exists(username):
        return {"body":{"message":"Username alrady exists"}, "status_code":401}
    else:
        password_hash = hash_string(password)
        print(username,password_hash)
        # db operation to insert the username and password_hash into db
        return {"body":{"message":"Registered Successfully"}, "status_code":200}

def check_username_exists(username):
    # db operation to check the username exists or not in db
    # return true if exists and false if not exists
    return False

def login_user(username,password):
    password_hash = hash_string(password)
    # db operation to check the credentials username and password_hash with in db
    # if True return {"body":{"message":"Login Successfully"}, "status_code":200}
    # else return {"body":{"message":"Inavlid Credentials"}, "status_code":401}
    return {"body":{"message":"Login Successfully"}, "status_code":200}

def insert_encryption(key,value):
    try:
        # insert key and value in seperate table 
        # use this table while impleting verfyCookie endpoint
        return True
    except:
        return False
    
def get_encryption(key):
    # get the encryption value using the key and return it as follows 
    # return signal is true and ecrypted string if it exists, False if it is not exists in db 
    return {"signal":True, "encrypted_string": ""}

def getDocuments(userId):
    # get user documents by userId
    userDocuments = [] # place the list of userDocuments in this list as of {"fileName":"jhgfghj", "fileId":"tggjnb","dateCreated":"khgfdfgh","ownerName":"kjhgfghj"}
    for document in userDocuments:
        # get shared users of this document
        sharedUsers = [] # place the list of sharedusers in this list as of {"userId": "hgfdfghj","permission":"jhgfhh,yghg"} 
        document["sharedUsers"]=sharedUsers

    return {"body":{"message":"Documents fetched Successfully", "filesList":userDocuments}, "status_code":200}

def getSharedDocuments(userId):
    # get user shared Documents by userId
    sharedDocuments = [] # place the list if shared Documents in this list of as of { "fileId":"tggjnb","ownerName":"kjhgfghj","permissions":"jvbnbvb,iughj"}
    for document in sharedDocuments:
        # get filename from userDocuments table using current document file id
        fileName = "" # put the file name here
        document["fileName"] = fileName 
        # get other users who shared with same document
        sharedUsers = [] # place the list of sharedusers in this list as of {"userId": "hgfdfghj","permission":"jhgfhh,yghg"} 
        document["sharedUsers"]=sharedUsers

    return {"body":{"message":"Documents fetched Successfully", "filesList":sharedDocuments}, "status_code":200}

def getDocumentContent(userId,fileId):
    # get the filecontent using fileId and userId
    fileContent = "" # place the file content in this 
    # if file exits with fileId 
    # return {"body":{"message":"Documents fetched Successfully", "fileId":fileId, "fileContent":fileContent}, "status_code":200}
    
    # else
    # return {"body":{"message":"File not found"}, "status_code":401}
    pass

def deleteDocument(userId,fileId):
    # first check the file is exist or not 
    # if not exists
    # return {"body":{"message":"File not found"}, "status_code":401}

    # if file exits delete the file in User Documents table and also Shared Documents Table
    # return {"body":{"message":"File Deleted Successfully"}, "status_code":200}
    pass

def renameDocument(userId,fileId):
    # first check the file is exist or not 
    # if not exists
    # return {"body":{"message":"File not found"}, "status_code":401}

    # if file exits rename the file in User Documents table
    # return {"body":{"message":"File Renamed Successfully"}, "status_code":200}
    pass

def updateFilePermissions(userId,fileId,sharedUsers):
    # first check the file is exist or not 
    # if not exists
    # return {"body":{"message":"File not found"}, "status_code":401}

    # if file exits 
    #       first delete all entries of this fileId in shared Documents Table,
    #       write all the entries to the shared Documents Table, as below
    for entry in sharedUsers:
        sharedUserId = entry["userId"]
        permission = entry["permission"]
        #put the data in table
    # return {"body":{"message":"File Renamed Successfully"}, "status_code":200}
    pass

def newFile(userId,fileName,dateCreated):
    # first check the user id is exits in user table or not 
    # if exists then put the above data in file table
    fileId = generate_alphanumeric_code()
    content = ""
    # return {"body":{"message":"File Created Successfully"}, "status_code":200}
    # if not exists then return {"body":{"message":"User not found"}, "status_code":401}

def saveDocumentContent(userId,fileId,content):
    # first check in files table, if the user is the owner of the fileid 
    # if yes update content here itself using a query
    # if not check in shared files table with fileid and user id 
    # if the user is mapped with file id, get the permission
    permission = "" # put the permission string here
    if "edit" in permission.split(","):
        # update the content in files table corresponding to the file id and return as follows
        return {"body":{"message":"File updated Successfully"},"status_code":200}
    else:
        return {"body":{"message":"User dosen't have sufficient privileges"},"status_code":403}
    pass