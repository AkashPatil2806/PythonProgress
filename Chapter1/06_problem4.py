import os

# 1. Define the directory path ('.' means the current working folder)
# You can change this to any absolute path like "C:/Users/Username/Documents" or "/home/user"
directory_path = 'C:' 

try:
    # 2. Fetch all files and folders inside the directory
    contents = os.listdir(directory_path)
    
    print(f"--- Contents of '{directory_path}' ---")
    
    # 3. Loop through the list and print each item
    for item in contents:
        print(item)
        
except FileNotFoundError:
    print(f"Error: The directory '{directory_path}' does not exist.")