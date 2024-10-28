import os, shutil
path = r"C:/Users/jespinoza/Documents/"
file_name = os.listdir(path)

folder_names = ['Excel Files', 'Ppt Files', 'Pdf Files', 'Csv Files']

for loop in range(0,4):
    if not os.path.exists(path + folder_names[loop]):
        print(path + folder_names[loop])
        os.makedirs(path + folder_names[loop])

for file in file_name:
    if ".xlsx" in file and not os.path.exists(path + "Excel Files/" + file):
        shutil.move(path + file, path + "Excel Files/" + file)
    elif ".ppt" in file and not os.path.exists(path + "Ppt Files/" + file):
        shutil.move(path + file, path + "Ppt Files/" + file)
    elif ".pdf" in file and not os.path.exists(path + "Pdf Files/" + file):
        shutil.move(path + file, path + "Pdf Files/" + file)
    elif ".csv" in file and not os.path.exists(path + "Csv Files/" + file):
        shutil.move(path + file, path + "Csv Files/" + file)
    else:
        print("There are files in this path that were not moved")




