# FILE SORTER AND ORGANISER

import os, shutil

# input your file directory below and add a slash at the end
# You can also change from backward slash to forward slash if path is copied from explorer
path = r"C:/Users/olatu/Desktop/File Sorter Project/File Sorter/"

# Check the files in the path/file sorter folder
file_names = os.listdir(path)

# Please include all the file types in this folder_name list if they dont already exist
folder_names = ['csv files', 'pdf files', 'text files', 'image files','audio files', 'video files']

# The lines below creates the folders in the folder names if they dont already exist in the path
for i in range(0, len(folder_names)):
    if not os.path.exists(path + folder_names[i]):
        os.makedirs(path + folder_names[i])

# The lines below moves the file into the created folders based on their format if thier path dont already exist.
for file in file_names:
    if ('.csv' in file)or ('.xlsl' in file) and not os.path.exists(path + 'csv files/' + file):
        shutil.move(path + file, path + 'csv files/'+ file)
    elif ('.pdf' in file) and not os.path.exists(path + 'pdf files/' + file):
        shutil.move(path + file, path + 'pdf files/'+ file)
    elif ('.txt' in file) or ('.docx' in file) and not os.path.exists(path + 'text files/' + file):
        shutil.move(path + file, path + 'text files/'+ file)
    elif ('.jpeg' in file) or ('.jpg' in file) or ('.png' in file) or ('.gif' in file) and not os.path.exists(path + 'image files/' + file):
        shutil.move(path + file, path + 'image files/'+ file)
    elif ('.mp3' in file) and not os.path.exists(path + 'audio files/' + file):
        shutil.move(path + file, path + 'audio files/'+ file)
    elif ('.mp4'  in file) and not os.path.exists(path + 'video files/' + file):
        shutil.move(path + file, path + 'video files/'+ file)
    else:
        print('All files have been sorted accordingly into the folders')
