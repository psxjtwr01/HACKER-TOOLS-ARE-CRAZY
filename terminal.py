import os
import sys
import webbrowser
import random
import datetime
import requests
import time
import getpass
from hacktrue import *

active = False

print("ACTIVATING COOL HACKER STUFF")

time.sleep(1)
for i in range(1000):
    for amount_of_zeros in range(random.randint(1,100)):
        sys.stdout.write(f"{random.randint(0,1)}")
def get_weather(location):
    if location.lower() == "here":
        location = "Arlington"
    write(requests.get(f"https://wttr.in/{location}").text)


def activate_hacks():
    global active
    active = True


def dc_hecks():
    write("|| Activating DC Hacker Tools ||")
    dccommands = {
        "0": lambda: None,
        "1": lambda: write(f"IP address: {get_ip()}"),
        "2": lambda path: write("File exists.")
        if exists(path)
        else write("File does not exist."),
        "3": lambda command: os.system(command),
        "4": lambda file: create_file(file),
        "5": lambda file: delete_file(file),
        "6": lambda drive: write("Changing  drive...") and os.chdir(f"{drive}"),
        "7": lambda old_name, new_name: rename_file(old_name, new_name),
        "8": lambda dir_name: create_directory(dir_name),
        "9": lambda dir_name: remove_directory(dir_name),
        "10": lambda: list_directory(),
    }

   

    
    xtrn(dccommands=dccommands)


users = {"admin": "admin", "charmander": "enter", "user3": "password3"}
hacker_commands = {"dc": {"function": lambda: dc_hecks()}}
commands = {
    "hello": {
        "description": "writes 'Hello, world!'",
        "function": lambda: write("Hello, world!"),
    },
    "cls": {"description": "Clears the terminal", "function": lambda: os.system("cls")},
    "google": {
        "description": "Opens a Google search in the default web browser",
        "function": lambda query: webbrowser.open(f"https://lmgtfy.app/?q={query}"),
    },
    "youtube": {
        "description": "Opens a YouTube search in the default web browser",
        "function": lambda query: webbrowser.open(
            f"https://www.youtube.com/results?search_query={query}"
        ),
    },
    "roll": {
        "description": "Rolls a die with the specified number of sides",
        "function": lambda sides: write(random.randint(1, int(sides))),
    },
    "time": {
        "description": "writes the current time",
        "function": lambda: write(datetime.datetime.now().strftime("%H:%M:%S")),
    },
    "weather": {
        "description": "writes the weather for the specified location",
        "function": lambda location: get_weather(location),
    },
    "cmds": {
        "description": "Executes a system command",
        "function": lambda command: os.system(command),
    },
    "hekrs": {"function": lambda: activate_hacks()},
}

# Define a function to clear the terminal screen
def clear(l=True):
    time.sleep(1.5)
    os.system("cls")
    print(  # cmd.cls() cmd.echo("logo")
        r"""

   _____     __       _                          _                _    __                         _        
  / ____| _  \ \     | |                        (_)              | |   \ \                       (_)       
 | |     (_)  \ \    | |_  ___  _ __  _ __ ___   _  _ __    __ _ | |    \ \     _ __ ___    __ _  _  _ __  
 | |           \ \   | __|/ _ \| '__|| '_ ` _ \ | || '_ \  / _` || |     \ \   | '_ ` _ \  / _` || || '_ \ 
 | |____  _     \ \  | |_|  __/| |   | | | | | || || | | || (_| || |      \ \  | | | | | || (_| || || | | |
  \_____|(_)     \_\  \__|\___||_|   |_| |_| |_||_||_| |_| \__,_||_|       \_\ |_| |_| |_| \__,_||_||_| |_|
                                                                                                         
                                                                                                                                                     
                                                                    
                                                          
          """
    )
    if l:
        write("Type 'help' to see a list of commands.")


clear(False)

# Prompt the user for their username and password
while True:
    write(r"Welcome to C:\terminal Hope you enjoy \03")
    username = input("Enter your username: ")
    if username != "bp":
        password = getpass.getpass("Enter your password: ")

        # Check if the username and password are valid
        if username in users and password == users[username]:
            if username == "admin" and password == "admin":
                hacker_command = True
            else:
                hacker_command = False
            write("Login successful!")

            clear()
            break
        else:
            write("Invalid username or password. Please try again.")
    else:
        clear()
        break
while True:

    # Prompt the user for a command
    user_input = input("Enter a command: ")
    if user_input == "help":
        write("Available commands:")
        for command, data in commands.items():
            if command != "hekrs":
                write(f"- {command}: {data['description']}")
    # Check if the user's input is a math expression
    try:
        result = eval(user_input)
        write(result)
    except:

        # If the input is not a math expression, check if it's a custom command
        parts = user_input.split()
        command = parts[0]
        args = parts[1:]
        if command in commands and command != "weather":
            commands[command]["function"](*args)
            time.sleep(2)
            clear()
        elif command in commands and command == "weather":
            commands[command]["function"](*args)
        # Check if the user's input is a hacker command
        elif hacker_command and command in hacker_commands:
            hacker_commands[command]["function"](*args)
        # Check if the user's input is a command creation statement
        elif "=" in user_input and "lambda" in user_input:
            try:
                # Use eval to create a new lambda function
                new_command = eval(user_input)
                # Extract the command name from the input
                command_name = user_input.split("=")[0].strip()
                # Add the new command to the dictionary of commands
                commands[command_name] = new_command
                write(f"Command '{command_name}' created.")
            except:
                sys.stderr.write("\033[91mInvalid command creation statement.\033[0m")
        # If the input is not a math expression or a custom command or a command creation statement, write an error message
        else:
            sys.stderr.write("\033[91m Invalid input. \033[0m")
