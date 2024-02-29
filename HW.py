import os
import logging
from collections import namedtuple

logging.basicConfig(filename='log.txt', level=logging.INFO)

FileData = namedtuple('FileData', ['name', 'extension', 'is_directory', 'parent_directory'])

def process_directory(path):
    files = os.listdir(path)
    
    for file in files:
        file_path = os.path.join(path, file)
        
        if os.path.isfile(file_path):
            name, extension = os.path.splitext(file)
            file_data = FileData(name=name, extension=extension, is_directory=False, parent_directory=path)
        else:
            file_data = FileData(name=file, extension='', is_directory=True, parent_directory=path)

        logging.info(file_data)
    
        if os.path.isdir(file_path):
            process_directory(file_path)

directory_path = input("Введите путь до директории: ")

process_directory(directory_path)