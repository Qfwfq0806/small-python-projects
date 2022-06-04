import os
import datetime

# this small app can help us delete the files of certain directory very quickly.
path = "/Users/apple/python"  #we can change the addresse here.
os.chdir(path) # go to the desired dir.

today = datetime.datetime.today()
print(today) #get today's date;

for root, dirs, files in os.walk(path, topdown=False):
    for name in files:
        if not name.endswith(".docx") and not name.endswith(".pdf") : #Here we don't delete the files ending with ".docx" or ".pdf"
           t = os.stat(os.path.join(root,name))[8]
           filetime = datetime.datetime.fromtimestamp(t) - today  #we get the date of the creation of certain files.
        
           if filetime.days <= -7 :
               print(os.path.join(root,name), filetime.days)
               os.remove(os.path.join(root,name))