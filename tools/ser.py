from colorama import Fore
import os
import platform
import re
import requests
import time
import shutil

def ser_menu():
    # Clear the terminal screen based on the operating system
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    
    # Display the user search tools menu
    print(f"""{Fore.MAGENTA}
          ▄• ▄▌.▄▄ · ▄▄▄ .▄▄▄      .▄▄ · ▄▄▄ . ▄▄▄· ▄▄▄   ▄▄·  ▄ .▄
          █▪██▌▐█ ▀. ▀▄.▀·▀▄ █·    ▐█ ▀. ▀▄.▀·▐█ ▀█ ▀▄ █·▐█ ▌▪██▪▐█
          █▌▐█▌▄▀▀▀█▄▐▀▀▪▄▐▀▀▄     ▄▀▀▀█▄▐▀▀▪▄▄█▀▀█ ▐▀▀▄ ██ ▄▄██▀▐█
          ▐█▄█▌▐█▄▪▐█▐█▄▄▌▐█•█▌    ▐█▄▪▐█▐█▄▄▌▐█ ▪▐▌▐█•█▌▐███▌██▌▐▀
           ▀▀▀  ▀▀▀▀  ▀▀▀ .▀  ▀     ▀▀▀▀  ▀▀▀  ▀  ▀ .▀  ▀·▀▀▀ ▀▀▀ ·                                               
  |--------------------------------------------------------------------------------------------|
  | [1] Sherlock - Find user profiles registered on various social media platforms.            |
  | [2] Nexfil - An OSINT tool to locate profiles by username.                                 |
  | [3] XR-Search - Custom user search tool.                                                   |
  | [00] Return to Main Menu                                                                   |
  | [99] Exit                                                                                  |
  |--------------------------------------------------------------------------------------------|
  """)
    
    # Get user input for the desired option
    var = input(f'\n{Fore.CYAN}root@KILLA_EZ:~# ')

    # Sherlock
    if var == "1":
        if os.path.exists('tools/sherlock'):
            print(f'\n{Fore.RED}[!] Sherlock is already installed.')
            ques = input(f'\n{Fore.GREEN}[?] Do you want to launch the tool? [Y/n]: ')
            if ques.lower() == "y":
                username = input('\n[~] Enter a username: ')
                if username.strip() == "":
                    print(f'\n{Fore.RED}[!] Error: You must enter a username.')
                else:
                    if platform.system() == "Linux":
                        os.system(f"python3 tools/sherlock/sherlock/sherlock.py {username}")
                    else:
                        os.system(f"python tools/sherlock/sherlock/sherlock.py {username}")
            else:
                ser_menu()
        else:
            print(f'\n{Fore.GREEN}[~] Installing Sherlock...')
            if platform.system() == "Linux":
                os.system("git clone https://github.com/sherlock-project/sherlock.git && mv 'sherlock' tools/ && pip3 install -r tools/sherlock/requirements.txt")
            else:
                os.system("git clone https://github.com/sherlock-project/sherlock.git")
                shutil.move("sherlock/", "tools")
                os.system("python -m pip install -r tools/sherlock/requirements.txt")
            print('\n[~] Sherlock installed successfully.')
            time.sleep(2)
            ser_menu()

    # Nexfil
    elif var == "2":
        if os.path.exists('tools/nexfil'):
            print(f'\n{Fore.RED}[!] Nexfil is already installed.')
            ques = input(f'\n{Fore.GREEN}[?] Do you want to launch the tool? [Y/n]: ')
            if ques.lower() == "y":
                username = input('\n[~] Enter a username: ')
                os.chdir('tools/nexfil')
                os.system(f"python3 nexfil.py -u {username}")
                os.chdir('../..')
            else:
                ser_menu()
        else:
            print(f'\n{Fore.GREEN}[~] Installing Nexfil...')
            os.system("git clone https://github.com/thewhiteh4t/nexfil.git && mv 'nexfil' tools/ && pip3 install -r tools/nexfil/requirements.txt")
            print('\n[~] Nexfil installed successfully.')
            time.sleep(2)
            ser_menu()

    # XR-Search
    elif var == "3":
        # Clear the screen
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

        # Display XR-Search logo
        logo = f"""{Fore.BLUE}
      ██   ██ ██████        ███████ ███████  █████  ██████   ██████ ██   ██ 
       ██ ██  ██   ██       ██      ██      ██   ██ ██   ██ ██      ██   ██ 
        ███   ██████  █████ ███████ █████   ███████ ██████  ██      ███████ 
       ██ ██  ██   ██            ██ ██      ██   ██ ██   ██ ██      ██   ██ 
      ██   ██ ██   ██       ███████ ███████ ██   ██ ██   ██  ██████ ██   ██"""
        print(logo)

        username = input('\n[~] Enter the username: ')
        sites = [
            f"https://github.com/{username}",
            f"https://twitter.com/{username}",
            f"https://instagram.com/{username}",
            f"https://www.reddit.com/user/{username}",
            f"https://www.pinterest.com/{username}",
            f"https://www.twitch.tv/{username}",
            f"https://xboxgamertag.com/search/{username}",
            f"https://open.spotify.com/user/{username}",
            f"https://www.roblox.com/user.aspx?username={username}",
            f"https://t.me/{username}",
            f"https://xvideos.com/profiles/{username}",
            f"https://www.youtube.com/user/{username}",
            f"https://gitlab.com/{username}",
            f"https://api.mojang.com/users/profiles/minecraft/{username}",
            f"https://www.codecademy.com/profiles/{username}",
            f"https://www.codewars.com/users/{username}",
            f"https://forum.hackthebox.eu/profile/{username}",
            f"https://replit.com/@{username}"
        ]
        
        # Search for the user across sites
        for url in sites:
            response = requests.get(url)
            if response.status_code == 200:
                print(f'\n{Fore.GREEN}[✔️] User found: {url}')
            else:
                print(f'\n{Fore.RED}[!] User not found: {url}')

    # Return to Main Menu
    elif var == "00":
        if platform.system() == "Linux":
            os.system("python3 KILLA_EZ.py")
        elif platform.system() == "Windows":
            os.system("python KILLA_EZ.py")
        else:
            exit()

    # Exit
    elif var == "99":
        exit()

    # Invalid Input
    else:
        print(f'\n{Fore.RED}[!] Error: Invalid option.')
        time.sleep(2)
        ser_menu()

