#!/usr/bin/env python3

############################################
#                                          # 
#        This is a tool used to            #             
#      INVESTIGATE a linux machine         # 
#                                          #     
#                           --r3tro-t3ch   #
#                                          # 
############################################

import os,sys,signal


class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


def handler( signal_recieved, frame ):

    print ( "\n" + colors.OKCYAN + "Type \"exit\" to exit" + colors.ENDC)
    return None 

def Main():
   
    signal.signal( signal.SIGINT, handler)




    print ()
    print ( colors.BOLD + colors.WARNING + "  _      _                     _____           _                   _____                    _   _             _             ")
    print ( " | |    (_)                   / ____|         | |                 |_   _|                  | | (_)           | |            ")
    print ( colors.FAIL + " | |     _ _ __  _   ___  __ | (___  _   _ ___| |_ ___ _ __ ___     | |  _ ____   _____ ___| |_ _  __ _  __ _| |_ ___  _ __ ")
    print ( colors.FAIL + " | |    | | '_ \| | | \ \/ /  \___ \| | | / __| __/ _ | '_ ` _ \    | | | '_ \ \ / / _ / __| __| |/ _` |/ _` | __/ _ \| '__|")
    print ( colors.FAIL + " | |____| | | | | |_| |>  <   ____) | |_| \__ | ||  __| | | | | |  _| |_| | | \ V |  __\__ | |_| | (_| | (_| | || (_) | |   ")
    print ( colors.WARNING + " |______|_|_| |_|\__,_/_/\_\ |_____/ \__, |___/\__\___|_| |_| |_| |_____|_| |_|\_/ \___|___/\__|_|\__, |\__,_|\__\___/|_|   ")
    print ( "                                      __/ |                                                        __/ |                    ")   
    print ( "                                     |___/                                                        |___/                     ")
    print ()
    print ( colors.OKCYAN + "                                                                                               -- by r3tro-t3ch             " + colors.ENDC)
    

    #checking root privilages
    if os.getuid() != 0 :
        
        print ( colors.FAIL + "Permission denied." + colors.ENDC)
        print ( colors.BOLD + colors.OKCYAN + "usage : sudo python3 " + sys.argv[0] + colors.ENDC)
        exit(0)

    #console

    print ( "print \"help\" or \"h\" for command list")


    while 1:

        command = str( input( "> "))

        #help

        if command == "help" or command == "h":

            print () 
            print (colors.BOLD + colors.OKBLUE + "Command list" + colors.ENDC)
            print () 
            print ("process_live  - prints all the live processes. Use \"Ctrl + c\" to exit live mode")
            print ("disk_list     - prints all the available disk partition")
            print ("sys_detail    - prints the summary of all the hardware details")
            print ("mem_check     - prints the memory usage")
            print ("mem_detail    - prints detailed memory usage. Use \"q or Q\" to exit from memory usage mode")
            print ("cpu_detail    - prints live cpu usage. Use \"Ctrl + c\" to exit live mode") 
            print ("help          - prints this message")
            print ("clear         - clears the current console screen")
            print ("exit          - exits from the tool")
            print ()

        elif command == "process_live":

            os.system("top")

        elif command == "disk_list":

           os.system("fdisk -l")

        elif command == "sys_detail":

            os.system("lshw -short")

        elif command == "mem_check":

            os.system("vmstat")

        elif command == "mem_detail":

            os.system("less /proc/meminfo")

        elif command == "cpu_details":

            os.system("cpustat")

        elif command == "exit" :

            exit(0)

        elif command == "clear":

            os.system("clear")

        elif command == "":

            pass

        else:

            print () 
            print (colors.BOLD + colors.OKBLUE + "Command list" + colors.ENDC)
            print () 
            print ("process_live  - prints all the live processes. Use \"Ctrl + c\" to exit live mode")
            print ("disk_list     - prints all the available disk partition")
            print ("sys_detail    - prints the summary of all the hardware details")
            print ("mem_check     - prints the memory usage")
            print ("mem_detail    - prints detailed memory usage. Use \"q or Q\" to exit from memory usage mode")
            print ("cpu_detail    - prints live cpu usage. Use \"Ctrl + c\" to exit live mode") 
            print ("help          - prints this message")
            print ("clear         - clears the current console screen")
            print ("exit          - exits from the tool")
            print ()
           
if __name__ == "__main__":

    Main()

