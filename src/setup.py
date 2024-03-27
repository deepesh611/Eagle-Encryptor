
import time
import lib
from colorama import Fore

print(Fore.GREEN + '\n\nModules Installed Successfully...')
time.sleep(1)

try:
    sql_pwd = lib.pwinput.pwinput(prompt ="\nENTER MySQL PASSWORD :\n", mask="*")
except:
    sql_pwd = input("\nENTER MySQL PASSWORD :\n")
    
lib.sql_setup(sql_pwd)
time.sleep(1)
print(Fore.GREEN + '\nSetup Completed...\n' + Fore.RESET)
time.sleep(2)

print(Fore.RED + 'If you run the Setup file again, your previous data of this program will be lost.\n' + Fore.RESET)
time.sleep(1)
print(Fore.LIGHTCYAN_EX + 'You can close this window and run the main program\nEnjoy Encrypting !\n\n  🔓🔑🔒 -> 🔐\n')
time.sleep(3)


