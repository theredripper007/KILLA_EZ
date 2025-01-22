from colorama import Fore
import os
import platform

def scan():
    # Clear the terminal screen based on the operating system
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    
    # Display the scanning menu
    print(f"""{Fore.MAGENTA}
   ▄████████  ▄████████    ▄████████ ███▄▄▄▄   ███▄▄▄▄      ▄████████    ▄████████ 
  ███    ███ ███    ███   ███    ███ ███▀▀▀██▄ ███▀▀▀██▄   ███    ███   ███    ███ 
  ███    █▀  ███    █▀    ███    ███ ███   ███ ███   ███   ███    █▀    ███    ███ 
  ███        ███          ███    ███ ███   ███ ███   ███  ▄███▄▄▄      ▄███▄▄▄▄██▀ 
▀███████████ ███        ▀███████████ ███   ███ ███   ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
         ███ ███    █▄    ███    ███ ███   ███ ███   ███   ███    █▄  ▀███████████ 
   ▄█    ███ ███    ███   ███    ███ ███   ███ ███   ███   ███    ███   ███    ███ 
 ▄████████▀  ████████▀    ███    █▀   ▀█   █▀   ▀█   █▀    ██████████   ███    ███ 
                                                                        ███    ███ 

  |--------------------------------------------------------------------------------------------|
  | [1] Port Scan                                                                              |
  | [2] Specific Port Scan                                                                     |
  | [3] Port Scan with Version Detection                                                      |
  | [4] Port Scan with OS Detection                                                           |
  | [5] Quick Scan (Open Ports Only)                                                          |
  | [6] Subnet Scan                                                                            |
  | [7] Stealth Scan                                                                           |
  | [8] TCP SYN Scan                                                                           |
  | [9] UDP Scan                                                                               |
  | [00] Return to Main Menu                                                                   |
  | [99] Exit                                                                                  |
  |--------------------------------------------------------------------------------------------|
    """)
    
    # Get user input for the scanning option
    var = input(f'\n{Fore.CYAN}root@KILLA_EZ:~# ')

    # Port Scan
    if var == "1":
        target = input("\n[~] Enter the host or IP to scan: ")
        os.system(f"nmap {target}")
    
    # Specific Port Scan
    elif var == "2":
        target = input("\n[~] Enter the host or IP to scan: ")
        ports = input("\n[~] Enter the ports to scan (comma-separated, e.g., 22,80,443): ")
        os.system(f"nmap -p {ports} {target}")
    
    # Port Scan with Version Detection
    elif var == "3":
        target = input("\n[~] Enter the host or IP to scan: ")
        os.system(f"nmap -sV {target}")
    
    # Port Scan with OS Detection
    elif var == "4":
        target = input("\n[~] Enter the host or IP to scan: ")
        os.system(f"nmap -O {target}")
    
    # Quick Scan (Open Ports Only)
    elif var == "5":
        target = input("\n[~] Enter the host or IP to scan: ")
        os.system(f"nmap -F {target}")
    
    # Subnet Scan
    elif var == "6":
        subnet = input("\n[~] Enter the subnet to scan (e.g., 192.168.1.0/24): ")
        os.system(f"nmap -sP {subnet}")
    
    # Stealth Scan
    elif var == "7":
        target = input("\n[~] Enter the host or IP to scan: ")
        os.system(f"nmap -sS {target}")
    
    # TCP SYN Scan
    elif var == "8":
        target = input("\n[~] Enter the host or IP to scan: ")
        os.system(f"nmap -sS -sV {target}")
    
    # UDP Scan
    elif var == "9":
        target = input("\n[~] Enter the host or IP to scan: ")
        os.system(f"nmap -sU {target}")
    
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
        scan()

