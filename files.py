import os
file_path = input("Enter file path: ")
news = input("Type any text: ")

if os.path.exists(file_path):
    print("file exists succesfully")
else:
    print("file dosn't exist")

