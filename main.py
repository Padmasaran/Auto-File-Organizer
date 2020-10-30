import os, time
from os import listdir
from os.path import isfile,join,isdir
import shutil

Directories = { 
    "Webpage": [".html5", ".html", ".htm", ".xhtml"], 
    "Images": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg", 
               ".heif", ".psd"], 
    "Videos": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", 
               ".qt", ".mpg", ".mpeg", ".3gp"], 
    "Documents": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods", 
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox", 
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", 
                  ".pptx",".csv"], 
    "Compressed": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", 
                 ".dmg", ".rar", ".xar", ".zip"], 
    "Audio": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", 
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"], 
    "Text": [".txt", ".in", ".out"], 
    "PDF": [".pdf"], 
    "Scripts": [".py",".sql",".ipynb",".pbix",".twbx"],  
    "Executable": [".exe",".msi"],
    "Books":[".epub",".mobi"]
}

Format_Mapping = {file_format: directory 
                for directory, file_formats in Directories.items() 
                for file_format in file_formats}

def FileOrganizer(mypath):
    #Retrieve all files in the source directory
    files = [item for item in listdir(mypath) if isfile(join(mypath,item))]
    #Retrieve the file format
    for i in files:
        file_format = '.'+str.lower(i.split('.')[-1])
        new_dir = Format_Mapping.get(file_format)
    #If not in mapping, assign as 'Misc'
        if new_dir is None:
            new_dir = 'Misc'
    #Construct paths
        source_path = join(mypath,i)
        target_dir_path = join(mypath,new_dir)
        target_path = join(target_dir_path,i)
    #Create directory is not exists
        if isdir(target_dir_path) == False:
            os.mkdir(target_dir_path)
    #Move the files
        shutil.move(source_path,target_path)

if __name__ == "__main__":
    #Provide your source directory here
    mypath = r'C:\Users\USER\Downloads'

    #Detect change by comparing with previous state
    before = dict ([(f, None) for f in os.listdir (mypath)])

    while 1:
        time.sleep (10)
        after = dict ([(f, None) for f in os.listdir (mypath)])
        added = [f for f in after if not f in before]
        if added: 
            FileOrganizer(mypath)
        before = after