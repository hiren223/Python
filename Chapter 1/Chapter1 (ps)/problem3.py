import os
 
#  Specify the directory you want to list

directory_path = '/python'

# List all files and directories in the specified directory
contents = os.listdir(directory_path)

# Print each file and directory name
for item in contents:
    print(item)