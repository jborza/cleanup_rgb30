import os
current_dir = os.getcwd()
for file_name in os.listdir(current_dir):
    if '(Japan)' in file_name:
        os.remove(file_name)