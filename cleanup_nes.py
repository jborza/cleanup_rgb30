import os
current_dir = 'c:\\temp\\nes\\' #os.getcwd()
for file_name in os.listdir(current_dir):
    if ('China' in file_name) or ('(Japan)' in file_name) or ('(Asia)' in file_name) or ('(Beta' in file_name):
        os.remove(current_dir + file_name)
        