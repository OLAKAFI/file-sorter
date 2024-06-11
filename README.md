# FILE SORTER PROJECT

# This project is a python code that helps to sort files in a specified folder path. The files are sorted based on their file formats and files are created in this respect.

# Step 1 (Line 7):
First the user will have to imput the folder path of the folder to be sorted in the path varribale. This can copied on the explorer bar when the user have navigated to the folder to be sorted. However, there might be a need to change the backward slash(\) to forward slash (/)
For example:
path = r"C:\Users\olatu\Desktop\File Sorter Project\File Sorter"
path = r"C:/Users/olatu/Desktop/File Sorter Project/File Sorter"

Also there is a need to add a slash at the end of the path if copied to promote effective navigation and continuity
For example:
path = r"C:/Users/olatu/Desktop/File Sorter Project/File Sorter/"

# Step 2 (Line 13):
Please input the prefered folder names into the **folder_names** varriable. Please note that the list in not exhaustive an can be modified according to the application and the file format involved
**folder_names** = ['csv files', 'pdf files', 'text files', 'image files','audio files', 'video files']


# Step 3 (Line 16 -18):
TThese line of codes creates the folders in the folder_names created above if they dont already exist in the path
for i in range(0, len(folder_names)):
    if not os.path.exists(path + folder_names[i]):
        os.makedirs(path + folder_names[i])

        
# Step 4 (Line 20 -25)
These line of codes moves the file into the created folders based on their format if thier path dont already exist. This project only considered the following formats (.csv,.xlsl,.pdf,.txt,.docx,.jpeg,.jpg,.png,.gif,.mp3,.mp4). Please note that the file format list in not exhaustive an can be modified according to the application and the file format involved


I hope this tool helps someone out there makes this day to day work easy



Regards
# Olatunbosun Kafisanwo
        
