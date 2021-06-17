import dropbox

class UploadData:
    def __init__(self, accesstoken):
        self.accesstoken = accesstoken

    def uploadFile(self, fileFrom, fileTo):
        dbx = dropbox.Dropbox(self.accesstoken)


        f = open(fileFrom, 'rb')
        dbx.files_upload(f.read(), fileTo)
        
def main():
    access_token = 'e9j1OoqSP7sAAAAAAAAAAV7MI_ATCv8CgpwBbvC4Qq2Z6C3GxX5KEo1sq8uyByAf'
    uploadData = UploadData(access_token)

    fileFrom = input("Enter the file name to upload :- ")
    fileTo = input("Enter the full path in dropbox to upload :- ")
    
    uploadData.uploadFile(fileFrom, fileTo)
    
    print("File successfully uploaded")


main()