#!/usr/bin/env python3
import optparse
import subprocess

def print_banner():
    banner = '''
    _____  ___________       _______      _______ 
   |  __ \|_   _|  __ \   /\|__   __|/\  |__   __|
   | |__) | | | | |__) | /  \  | |  /  \    | |   
   |  ___/  | | |  _  / / /\ \ | | / /\ \   | |   
   | |     _| |_| | \ \/ ____ \| |/ ____ \ _| |_  
   |_|    |_____|_|  \/_/    \_\_/_/    \_\_____|

   Xyrth Rules Toolkit
    '''
    print(banner)

def run_nmap_scan(tgtHost, tgtPorts):
    try:
        tgtPorts = ','.join(tgtPorts)
        command = f'nmap -p {tgtPorts} {tgtHost}'
        subprocess.run(command, shell=True)
    except KeyboardInterrupt:
        print("\nScan terminated by user")
        exit()

def run_john_crack(password_file):
    try:
        command = f'john {password_file}'
        subprocess.run(command, shell=True)
    except KeyboardInterrupt:
        print("\nCracking terminated by user")
        exit()

def main():
    print_banner()

    parser = optparse.OptionParser('usage %prog -H <target> -p <port(s)> | -j <password_file>')
    parser.add_option("-H", dest="tgtHost", type="string", help="Specify target host")
    parser.add_option("-p", dest="tgtPorts", type="string", help="Specify target port(s) separated by comma")
    parser.add_option("-j", dest="passwordFile", type="string", help="Specify the password file for John the Ripper")

    (options, args) = parser.parse_args()

    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPorts).split(',')
    password_file = options.passwordFile

    if tgtHost and tgtPorts[0]:
        run_nmap_scan(tgtHost, tgtPorts)
    elif password_file:
        run_john_crack(password_file)
    else:
        print(parser.usage)
        exit()

if __name__ == "__main__":
    main()
