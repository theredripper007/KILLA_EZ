from colorama import Fore
import os
import platform
import time
import shutil

def phish():
    # Clear the terminal screen based on the operating system
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    
    # Display the phishing tools menu
    print(f"""{Fore.MAGENTA}

          ██████╗ ██╗  ██╗██╗███████╗██╗  ██╗██╗███╗   ██╗ ██████╗ 
          ██╔══██╗██║  ██║██║██╔════╝██║  ██║██║████╗  ██║██╔════╝ 
          ██████╔╝███████║██║███████╗███████║██║██╔██╗ ██║██║  ███╗
          ██╔═══╝ ██╔══██║██║╚════██║██╔══██║██║██║╚██╗██║██║   ██║
          ██║     ██║  ██║██║███████║██║  ██║██║██║ ╚████║╚██████╔╝
          ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
                                                         

  |--------------------------------------------------------------------------------------------|
  | [1] SayCheese - Tool for capturing an IP and a photo via the webcam.                       |
  | [2] Zphisher  - Phishing tool with over 30 login page templates.                           |
  | [3] 0ni-Phish - Tool with 10 login page templates, including 4 in Spanish!                |
  | [4] PyPhisher - Phishing tool with over 50 login page templates!                          |
  | [00] Return to the main menu                                                              |
  | [99] Exit                                                                                 |
  |--------------------------------------------------------------------------------------------|
  """)
    
    # Get user input for tool selection
    var = input(f'\n{Fore.CYAN}root@KILLA_EZ:~# ')

    # SayCheese
    if var == "1":
        if os.path.exists('tools/saycheese'):
            print(f'\n{Fore.RED}[!] SayCheese already exists.')
            ques = input(f'\n{Fore.GREEN}[?] Do you want to launch the tool? [Y/n]: ')
            if ques.lower() == "y":
                os.system("bash tools/saycheese/saycheese.sh")
            else:
                phish()
        else:
            if platform.system() == "Linux":
                print(f'\n{Fore.GREEN}[~] Installing SayCheese...')
                os.system("git clone https://github.com/hangetzzu/saycheese && mv 'saycheese' tools/")
                print('\n[~] SayCheese installed successfully.')
                time.sleep(2)
                phish()
            else:
                print(f'\n{Fore.RED}[!] SayCheese is not available for your operating system.')

    # Zphisher
    elif var == "2":
        if os.path.exists('tools/zphisher'):
            print(f'\n{Fore.RED}[!] Zphisher already exists.')
            ques = input(f'\n{Fore.GREEN}[?] Do you want to launch the tool? [Y/n]: ')
            if ques.lower() == "y":
                os.chdir('tools/zphisher')
                os.system("bash zphisher.sh")
                os.chdir('../..')
                os.system("python3 KILLA_EZ.py")
            else:
                phish()
        else:
            if platform.system() == "Linux":
                print(f'\n{Fore.GREEN}[~] Installing Zphisher...')
                os.system("git clone https://github.com/htr-tech/zphisher && mv 'zphisher' tools/")
                print('\n[~] Zphisher installed successfully.')
                time.sleep(2)
                phish()
            else:
                print(f'\n{Fore.RED}[!] Zphisher is not available for your operating system.')

    # 0ni-Phish
    elif var == "3":
        if os.path.exists('tools/0ni-Phish'):
            print(f'\n{Fore.RED}[!] 0ni-Phish already exists.')
            ques = input(f'\n{Fore.GREEN}[?] Do you want to launch the tool? [Y/n]: ')
            if ques.lower() == "y" and platform.system() == "Linux":
                os.system("python3 tools/0ni-Phish/0ni.py")
            else:
                phish()
        else:
            if platform.system() == "Linux":
                print(f'\n{Fore.GREEN}[~] Installing 0ni-Phish...')
                os.system("git clone https://github.com/Euronymou5/0ni-Phish && mv '0ni-Phish' tools/")
                print('\n[~] 0ni-Phish installed successfully.')
                time.sleep(2)
                phish()
            else:
                print(f'\n{Fore.RED}[!] 0ni-Phish is not available for your operating system.')

    # PyPhisher
    elif var == "4":
        if os.path.exists('tools/PyPhisher'):
            print(f'\n{Fore.RED}[!] PyPhisher already exists.')
            ques = input(f'\n{Fore.GREEN}[?] Do you want to launch the tool? [Y/n]: ')
            if ques.lower() == "y" and platform.system() == "Linux":
                os.chdir('tools/PyPhisher')
                os.system("python3 pyphisher.py")
                os.chdir('../..')
                os.system("python3 KILLA_EZ.py")
            else:
                phish()
        else:
            if platform.system() == "Linux":
                print(f'\n{Fore.GREEN}[~] Installing PyPhisher...')
                os.system(
                    "git clone https://github.com/KasRoudra/PyPhisher && mv 'PyPhisher' tools/ && pip3 install -r tools/PyPhisher/files/requirements.txt"
                )
                print('\n[~] PyPhisher installed successfully.')
                time.sleep(2)
                phish()
            else:
                print(f'\n{Fore.RED}[!] PyPhisher is not available for your operating system.')

    # Return to the main menu
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
        phish()

