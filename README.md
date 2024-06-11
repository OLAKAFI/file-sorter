# FILE SORTER PROJECT

# This project is a python code that helps to sort files in a specified folder path. The files are sorted based on their file formats and files are created in this respect.

# First the user will have to imput the folder path of the folder to be sorted in the path varribale. This can copied on the explorer bar when the user have navigated to the folder to be sorted. However, there might be a need to change the backward slash(\) to forward slash (/)
For example:
path = r"C:\Users\olatu\Desktop\File Sorter Project\File Sorter"
path = r"C:/Users/olatu/Desktop/File Sorter Project/File Sorter"

#Also there is a need to add a slash at the end of the path if copied to promote effective navigation and continuity
For example:
path = r"C:/Users/olatu/Desktop/File Sorter Project/File Sorter/"


# Also, the user of this project will have to input the prefered folder names into the folder_names varriable
# Please note that the list in not exhaustive an can be modified according to the application and the file format involved
folder_names = ['csv files', 'pdf files', 'text files', 'image files','audio files', 'video files']


# The lines below creates the folders in the folder_names created above if they dont already exist in the path
for i in range(0, len(folder_names)):
    if not os.path.exists(path + folder_names[i]):
        os.makedirs(path + folder_names[i])

        
# The lines below moves the file into the created folders based on their format if thier path dont already exist. This project only considered the following formats (.csv,.xlsl,.pdf,.txt,.docx,.jpeg,.jpg,.png,.gif,.mp3,.mp4). Please note that the file format list in not exhaustive an can be modified according to the application and the file format involved
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


I hope this tool helps someone out there makes this day to day work easy

Regards
Olatunbosun Kafisanwo
        
