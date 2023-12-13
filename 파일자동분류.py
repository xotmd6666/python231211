import os
import shutil
from glob import glob

def move_files(source_folder, destination_folder, file_extensions):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for ext in file_extensions:
        files = glob(os.path.join(source_folder, f'*.{ext}'))
        for file_path in files:
            shutil.move(file_path, destination_folder)

if __name__ == "__main__":
    download_folder = "C:/Users/Student/Downloads"
    images_folder = "C:/Users/Student/Downloads/images"
    data_folder = "C:/Users/Student/Downloads/data"
    docs_folder = "C:/Users/Student/Downloads/docs"

    # Move *.jpg, *.jpeg to \images folder
    move_files(download_folder, images_folder, ["jpg", "jpeg"])

    # Move *.csv, *.xlsx to \data folder
    move_files(download_folder, data_folder, ["csv", "xlsx"])

    # Move *.pdf to \docs folder
    move_files(download_folder, docs_folder, ["pdf"])
