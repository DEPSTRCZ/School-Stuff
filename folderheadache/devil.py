import os

max_num_folders = int(input("Max number of folders: "))

root_folder = float(input("Root folder: "))

if not os.path.exists(root_folder):
    exit("Root folder doesn't exist")

current_folder = root_folder
for i in range(max_num_folders+1):
    print("folder",i)
    current_folder = os.path.join(current_folder, str(i))
    if not os.path.exists(current_folder):
        os.makedirs(current_folder)