import os, time, sys
#from os import listdir
#from os.path import isfile, join

#python delete old files
#python delete old files
#python delete older files

#Method 1
folder_path = "C:\Files_To_Read"
now = time.time()
how_many_days_old_logs_to_remove = 7

only_files = []
for file in os.listdir(folder_path):
    file_full_path = os.path.join(folder_path,file)
    if os.path.isfile(file_full_path) and file.endswith(".txt"):
        if os.stat(file_full_path).st_mtime < now - how_many_days_old_logs_to_remove * 86400: #Delete files older than 7 days
             os.remove(file_full_path)
             print "\n File Removed : " , file_full_path
