import time
import subprocess
import threading
import sys


# TO RUN A COMMAND IN POWERSHELL
def run_command(command):
    """
    Run a command in Command Prompt.

    Parameters:
    - cmd (str): The command to be executed.

    Returns:
    - return_code (int): The return code of the command execution.
    - output (str): The standard output of the command.
    """
        
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, error = process.communicate()
    return process.returncode, output + error



def loading_animation():
    l = r'/-\|'
    while not installation_complete:
        for i in l:
            print('Installing Required Libraries ' + i, end='\r', flush=True)
            time.sleep(0.1)
            sys.stdout.write("\033[K")


# FUNCTION TO INSTALL ALL THE REQUIRED LIBRARIES
def install_libs():
    global installation_complete
    installation_complete = False

    try:
        # Start the loading animation in a separate thread
        loading_thread = threading.Thread(target=loading_animation)
        loading_thread.start()

        return_code, output = run_command('pip install -r ./requirements.txt')

        if return_code == 0:
            print(f"\nCommand 'pip install -r ./requirements.txt' executed successfully.\n\n{output}")
        else:
            print(f"\nError: Command 'pip install -r ../requirements.txt' failed with return code {return_code}. Output:\n{output}")
            time.sleep(5)
            exit()

    except Exception as e:
        print(f'\nError in installing required libraries: {str(e)}\nPlease refer to the README file for manual installation of libraries.\n')
        time.sleep(6)
        exit()

    finally:
        # Signal that the installation is complete
        installation_complete = True
        # Wait for the loading thread to finish
        loading_thread.join()


print('\n\n',time.ctime(),'\n')
install_libs()
time.sleep(2)

from colorama import Fore

print(Fore.GREEN + 'Modules Installed Successfully...')
time.sleep(1)


import lib

try:
    sql_pwd = lib.pwinput.pwinput(prompt ="\nENTER MySQL PASSWORD :\n", mask="*")
except:
    sql_pwd = input("\nENTER MySQL PASSWORD :\n")
    
lib.sql_setup(sql_pwd)

print(lib.Fore.GREEN + 'Setup Completed...\n' + lib.Fore.RESET)
time.sleep(2)

print('If you run the Setup file again, your previous data of this program will be lost.\n')
time.sleep(1)
print('You can close this window and run the main program\nEnjoy Encrypting !\n\n  🔓🔑🔒 -> 🔐\n')
time.sleep(3)

input('Press Enter to Exit...')