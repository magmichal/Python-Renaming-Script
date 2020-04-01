import os
FOLDER_PATH = "/"
if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(FOLDER_PATH))
    file_list = []

    #walk()

    for root, dirs, files in os.walk(FOLDER_PATH):
        for file in files:
            if file.endswith(".jpg"):
                new = os.path.join(root, file)
                print(new)
                file_list.append(new)

main()

#So far, this can only get and print the directory address. 
#For renaming, the script would need to parse through the last couple parts of the file path name and append it to a string. 
#When this is done, the name of of the file will be changed to the string. 
