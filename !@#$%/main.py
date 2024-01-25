
# importing required modules
import lib
import time


# calling some intro functions
lib.ascii_art()
lib.time.sleep(1)
lib.check()
lib.intro()


# main loop
while True:
    # lib.menu()                                                        # uncomment this line to show menu every time
    choice = input('\nEnter your command : ').lower()                 # taking input from user using any case
    print('')
    
    if choice == 'encf' or choice == 'ef':
        lib.encrypt()
        time.sleep(1)
    elif choice == 'decf' or choice == 'df':
        lib.decrypt()
        time.sleep(1)
    elif choice == 'view' or choice == 'v':
        lib.view_file_list()
        time.sleep(1)
    elif choice == 'add' or choice == 'a':
        lib.add_file()
        time.sleep(1)
    elif choice == 'del' or choice == 'd':
        lib.delete_file()
        time.sleep(1)
    elif choice == 'pwd' or choice == 'cp':
        lib.cng_pwd()
        time.sleep(1)
    elif choice == 'delall' or choice == 'da':
        lib.delete_all()
        time.sleep(1)
    elif choice == 'quit' or choice == 'q' or choice == 'exit':
        lib.outro('./Outro tags.txt')
        time.sleep(5)
        quit()
    elif choice == 'help' or choice == 'ls' or choice == 'menu':
        lib.menu()
        time.sleep(1)
    else:
        print(lib.Fore.RED + 'Command Not Found!\n' + lib.Fore.RESET)
        time.sleep(1)

    