import cv2
import time 
import random
import dropbox

startTime=time.time()
def takeSnapshot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        
        ret,frame=videoCaptureObject.read()
        imageName='img'+str(number)+'.png'
        cv2.imwrite(imageName,frame)
        startTime=time.time()
        result=False
    return imageName
    print("SNAPSHOT TAKEN")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

takeSnapshot()

def UploadFile(imageName):
    access_token='sl.AvZXdBFkN804NgH90pgSFF5wRGOHwE51isPQTtz8KPyQDkSWEdJlVrDwKx2Sz8r7uMA_Hso6pijtcKS78Igfyz1f0xoZo0_Xu5gaZKkI6nPmWcbL1dWrwUId8BUefRhPjMQ-Krc'
    file=image_counter
    fileFrom=file
    fileTo='PicsFolder/'+(imageName)
    dbx=dropbox.Dropbox(access_token)
    with open(fileFrom,'rb') as f:
        dbx.files_upload(f.read(),fileTo,mode=dropbox.files.WriteMode.overwrite)
        print("FILE UPLOADED")
def main():
    while (True):
        if (time.time()-startTime>=300):
            Name=takeSnapshot()
            UploadFile(Name)

main()