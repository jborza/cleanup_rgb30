import os
import re
import shutil
# codes for file versions: https://www.emutalk.net/threads/what-does-o1-h1-h2-and-o3-mean.4015/

# Get the current directory
current_dir = os.getcwd()

deleted_files = []

related_files = []


def cleanup(file_name):
    # Clean the file name
    cleaned_file_name = file_name
    cleaned_file_name = re.sub(r' \(.*\)', '', cleaned_file_name)
    cleaned_file_name = re.sub(r' \[.*\]', '', cleaned_file_name)
    cleaned_file_name = re.sub(r'.smd', '', cleaned_file_name)
    cleaned_file_name = re.sub(r'.bin', '', cleaned_file_name)
    return cleaned_file_name


# Iterate over each file in the current directory
for file_name in os.listdir(current_dir):
    # Check if the item is a megadrive file
    if not file_name.endswith('.smd') and not file_name.endswith('.bin'):
        continue
    # skip pre-release files
    if '(pre-release)' in file_name:
        deleted_files.append(file_name)
        continue
    if not os.path.isfile(os.path.join(current_dir, file_name)):
        continue

    # Clean the file name
    cleaned_file_name = cleanup(file_name)
    #print(file_name)

    # find the related files
    if len(related_files) == 0:
        related_files.clear()
        related_files.append(file_name)
        continue

    cleaned_related_file_name = cleanup(related_files[0])
    if (cleaned_file_name != cleaned_related_file_name):
        related_files.clear()
        related_files.append(file_name)
        continue
    #print('Related files to:', file_name)
    # check if the related file is the same as the filename
    if cleaned_related_file_name == cleaned_file_name:
        deleted_files.append(file_name)
        continue
    related_files.append(file_name)


print('Deleted files:')
if not os.path.exists('deleted'):
    os.mkdir('deleted')
for file in deleted_files:
    print(file)
    os.rename(file, 'deleted/' + file)
    