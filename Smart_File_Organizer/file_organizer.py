import os
import shutil

file_types = {
    "Images":[".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Document": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Videos":[".mp4", ".mov", ".avi", ".mkv"],
    "Music":[".mp3", ".wav", ".acc", ".flac"],
}

folder_path = input("Enter the folder path to organize: ")

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    if not os.path.isfile(file_path):
        continue
    name, ext = os.path.splitext(filename)
    ext = ext.lower()

    destination_folder = "Others"

    for folder, extensions in file_types.items():
        if ext in extensions:
            destination_folder = folder
            break

    destination_path = os.path.join(folder_path, destination_folder)
    os.makedirs(destination_path, exist_ok=True)
    shutil.move(file_path, os.path.join(destination_path, filename))

    print(f"Moved: {filename} --> {destination_folder}")