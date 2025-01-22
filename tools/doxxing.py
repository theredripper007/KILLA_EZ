from colorama import Fore
import os
import platform
import time
import shutil


def doxxer():
    # Clear the terminal based on the OS
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    
    # Menu header and options
    print(f"""{Fore.RED}
        ▄▀▀█▄▄   ▄▀▀▀▀▄   ▄▀▀▄  ▄▀▄  ▄▀▀▄  ▄▀▄  ▄▀▀█▀▄    ▄▀▀▄ ▀▄  ▄▀▀▀▀▄   
        █ ▄▀   █ █      █ █    █   █ █    █   █ █   █  █  █  █ █ █ █         
        ▐ █    █ █      █ ▐     ▀▄▀  ▐     ▀▄▀  ▐   █  ▐  ▐  █  ▀█ █    ▀▄▄  
          █    █ ▀▄    ▄▀      ▄▀ █       ▄▀ █      █       █   █  █     █ █ 
         ▄▀▄▄▄▄▀   ▀▀▀▀       █  ▄▀      █  ▄▀   ▄▀▀▀▀▀▄  ▄▀   █   ▐▀▄▄▄▄▀ ▐ 
        █     ▐             ▄▀  ▄▀     ▄▀  ▄▀   █       █ █    ▐   ▐         
        ▐                  █    ▐     █    ▐    ▐       ▐ ▐                  

  |--------------------------------------------------------------------------------------------|
  | [1] Doxxer-Toolkit - Complete doxxing toolkit for Linux and Termux.                        |
  | [2] Garuda - Doxxing tool for: full name, IP, phone number, and more.                      |
  | [3] LineX - Tool to gather information from a phone number.                                |
  | [4] IPlogger - Terminal-based IP logger for Linux and Termux.                              |
  | [00] Return to the main menu                                                               |
  | [99] Exit                                                                                  |
  |--------------------------------------------------------------------------------------------|
  """)
    
    # User input for tool selection
    var = input(f'\n{Fore.BLUE}root@KILLA_EZ:~# ')

    # Doxxer-Toolkit
    if var == "1":
        if os.path.exists('tools/Doxxer-Toolkit'):
            print(f'\n{Fore.RED}[!] Doxxer-Toolkit already exists.')
            ques = input(f'\n{Fore.GREEN}[?] Would you like to start the tool? [Y/n]: ')
            if ques.lower() == "y":
                os.system("python3 tools/Doxxer-Toolkit/dox.py")
            else:
                doxxer()
        else:
            if platform.system() == "Linux":
                print(f'\n{Fore.GREEN}[~] Installing Doxxer-Toolkit...')
                os.system(
                    "git clone https://github.com/Euronymou5/Doxxer-Toolkit && mv 'Doxxer-Toolkit' tools/ && bash tools/Doxxer-Toolkit/install.sh"
                )
                print('\n[~] Doxxer-Toolkit installed successfully.')
                time.sleep(2)
                doxxer()
            else:
                print(f'\n{Fore.RED}[!] Doxxer-Toolkit is not supported on your operating system.')

    # Garuda
    elif var == "2":
        if os.path.exists('tools/Garuda'):
            print(f'\n{Fore.RED}[!] Garuda already exists.')
            ques = input(f'\n{Fore.GREEN}[?] Would you like to start the tool? [Y/n]: ')
            if ques.lower() == "y":
                print("""
        Arguments:

        --name     Dox full name

        --ip       Dox an IP address

        --mail     Dox an email

        --phone    Dox a phone number

        --user     Dox a username
        """)
                arg = input(f'{Fore.BLUE}\n[~] Enter an argument for Garuda: ')
                if arg in ["--name", "--ip", "--mail", "--phone", "--user"]:
                    os.system(f"python3 tools/Garuda/garuda.py {arg}")
                else:
                    print(f'\n{Fore.RED}[!] Error: You must enter a valid argument.')
                    time.sleep(2)
                    doxxer()
            else:
                doxxer()
        else:
            if platform.system() == "Linux":
                print(f'\n{Fore.GREEN}[~] Installing Garuda...')
                os.system(
                    "git clone https://github.com/noob-coder123/Garuda && mv 'Garuda' tools/ && pip install -r tools/Garuda/requirements.txt "
                )
                print(f'\n[~] Garuda installed successfully.')
                time.sleep(2)
                doxxer()
            else:
                print(f'\n{Fore.RED}[!] Garuda is not supported on your operating system.')

    # LineX
    elif var == "3":
        if os.path.exists('tools/LineX'):
            print(f'\n{Fore.RED}[!] LineX already exists.')
            ques = input(f'\n{Fore.GREEN}[?] Would you like to start the tool? [Y/n]: ')
            if ques.lower() == "y":
                if platform.system() == "Linux":
                    os.system("python3 tools/LineX/linex.py")
                elif platform.system() == "Windows":
                    os.system("python tools/LineX/linex_win.py")
            else:
                doxxer()
        else:
            if platform.system() == "Linux":
                print(f'\n{Fore.GREEN}[~] Installing LineX...')
                os.system(
                    "git clone https://github.com/Euronymou5/LineX.git && mv 'LineX' tools/ && pip install requests"
                )
                print('\n[~] LineX installed successfully.')
                time.sleep(2)
                doxxer()
            elif platform.system() == "Windows":
                print(f'\n{Fore.GREEN}[~] Installing LineX...')
                os.system("git clone https://github.com/Euronymou5/LineX.git")
                shutil.move("LineX/", "tools")
                os.system("pip install requests")
                print('\n[~] LineX installed successfully.')
                time.sleep(2)
                doxxer()
            else:
                print(f'\n{Fore.RED}[!] LineX is not supported on your operating system.')

    # IPlogger
    elif var == "4":
        if os.path.exists('tools/IPlogger'):
            print(f'\n{Fore.RED}[!] IPlogger already exists.')
            ques = input(f'\n{Fore.GREEN}[?] Would you like to start the tool? [Y/n]: ')
            if ques.lower() == "y":
                os.system("python3 tools/IPlogger/run.py")
            else:
                doxxer()
        else:
            if platform.system() == "Linux":
                print(f'\n{Fore.GREEN}[~] Installing IPlogger...')
                os.system(
                    "git clone https://github.com/Euronymou5/IPlogger && mv 'IPlogger' tools/"
                )
                print('\n[~] IPlogger installed successfully.')
                time.sleep(2)
                doxxer()
            else:
                print(f'\n{Fore.RED}[!] IPlogger is not supported on your operating system.')

    # Return to main menu
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

    # Invalid input
    else:
        print(f'\n{Fore.RED}[!] Error: Invalid option.')
        time.sleep(2)
        doxxer()

