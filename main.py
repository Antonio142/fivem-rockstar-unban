# V0.1 LOGOUT ROCKSTAR ACCOUNT FOR FIVEM!

import colorama
from colorama import Fore, Back, Style
import os
from os import path
import time

def clearconsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

pathdDigitalEntitlements = os.getenv('LOCALAPPDATA') + "\DigitalEntitlements"

print(f"{Style.RESET_ALL}[{Fore.YELLOW}!{Style.RESET_ALL}] {Fore.WHITE}Welcome back, " + os.getlogin())
time.sleep(1.5)
clearconsole()

if path.exists(pathdDigitalEntitlements):
    print(f"{Style.RESET_ALL}[{Fore.YELLOW}!{Style.RESET_ALL}] {Fore.WHITE}Removing account...")
    os.rmdir(pathdDigitalEntitlements)
    print(f"{Style.RESET_ALL}[{Fore.YELLOW}!{Style.RESET_ALL}] {Fore.GREEN}Removed!, closing in 3 seconds...")
    time.sleep(3)
else:
    print(f"{Style.RESET_ALL}[{Fore.YELLOW}!{Style.RESET_ALL}] {Fore.RED}We couldnt find an account, closing in 3 seconds...")
    time.sleep(3)
