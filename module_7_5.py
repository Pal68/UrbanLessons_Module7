import os
import time

directory ='.'
for root, dirs, files in os.walk(directory):
        for file in files:
            file_name = os.path.join(root, file.title())
            filetime =  time.strftime("%d.%m.%Y %H:%M", time.localtime(os.path.getmtime(file_name)))
            file_size = os.path.getsize(file_name)
            parent_dir = os.path.dirname(file_name)
            print(f"Обнаружен файл: {file}, путь: {file_name}, размер: {file_size}, "
                  f"время изменения: {filetime}, родительская директория: {parent_dir}" )




