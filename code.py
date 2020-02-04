import os
from shutil import copyfile

for root, _, files in os.walk(r"ROMs/"):
    for name in files:
        file_without_extension = os.path.splitext(name)[0]

        with open('ROM_list.txt') as f:
            for line in f.readlines():
                print(line.rstrip())

                if file_without_extension.lower() == line.rstrip().lower():

                    copyfile(os.path.join(root, name),
                             os.path.join(r'Selected_ROMs/', name))
