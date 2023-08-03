#
# At a high level this file will take a username and password credential
# and a cloud URL where the file needs to be read from and do the needful to 
# create/update/delete the file
# The function will return "true " or success if passed. And error message if failed. 
#

import sys
import requests
import json
import time

def api_rwcd(username, pwd, cloudurl, filename, action_verb):
    if username == " ":
        return("Blank username")
    if pwd == " ":
        return("Blank pwd")
    if cloudurl == " ":
        return("Blank cloudurl")
    if filename == " ":
        return("Blanks filename")
    
    # Json serialises the content to be sent to the API
    #api_url = "https://crudfilecm-myngjq8fkmetutwyhddsi8949q86cuse2a-s3alias"
    api_url = "https://o07nhs9l4l.execute-api.us-east-2.amazonaws.com/uploads"
    headers =  {"Content-Type":"application/json"}
    
    response = requests.get(api_url)
    print("Response:", response.status_code)
    #print("Response json:", response.json())
                
    json_data = response.json()
    uploadURL = json_data['uploadURL']
    print(uploadURL)
    if action_verb == "get":
            try:
                print(uploadURL)
                return
            except FileNotFoundError:
                return("File not opened read") 
    elif action_verb == "create":
            try:
                f = open(filename, "r+")
                lines_from_file = f.readlines()
                f.close()
                print(str(time.time()))
                filejson = {"userId": str(time.time()), "filename": filename, "data_file": str(lines_from_file)}
                response = requests.put(uploadURL, data=json.dumps(filejson), headers=headers)
                print("Response:", response.status_code)
                
                return
            except FileNotFoundError:
                return("File not opened update") 
    elif action_verb == "delete":
            try:
                response = requests.delete(api_url)
                print("Response:", response.status_code)
                return
            except FileNotFoundError:
                return("File not opened delete") 
    elif action_verb == "download":
            try:
                
                return
            except FileNotFoundError:
                return("File not opened read") 
    print("File operation Successful")
    return

           
if (__name__ == "__main__"):
    print("Number of arguments:" + str(len(sys.argv)) + "arguments.")
    if (len(sys.argv) < 4):
        print("Please enter 3 arguments for the function: 1. Storage Cloud Name 2. File Path 3. Operation: create, read, update, delete")
        
    
    print("Argument List:%s %s %s", sys.argv[1], sys.argv[2], sys.argv[3])
    
    # Access cred is read from csv file
    
    f = open("/Users/priyashastri/Downloads/pshastri_accessKeys.csv", "r")
    Line1 = f.readline()
    Line2 = f.readline()
    
    access_cred = Line2.split(",")
    print(access_cred)
    f.close()
    
    # Call to api_rwcd to do the needful
    
    api_rwcd(access_cred[0], access_cred[1], sys.argv[1], sys.argv[2], sys.argv[3])
    
