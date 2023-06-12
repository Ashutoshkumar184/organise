import os
import shutil

fromsource = "C:\\Users\\rajiv\\Downloads\\C102_assets-main\\C102_assets-main"
destination="C:\\Users\\rajiv\\Downloads\\images"
listoffiles= os.listdir(fromsource)
print(listoffiles) 
for file_name in listoffiles:
    name,extension= os.path.splitext(file_name)
    if extension=='':
        continue
    if  extension in ['.gif','.png','.jpg','.jpeg','.jfif']:
        path1=fromsource+'/'+file_name
        path2=destination+'/'+"Image_files"
        path3=destination+'/'+"Image_file"+'/'+file_name

        if os.path.exists(path2):
            print("moving "+file_name+".............")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving "+file_name+".................")
            shutil.move(path1,path3)    
