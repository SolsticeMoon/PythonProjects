# Program to check the strength of passwords
# Requested by: Teacher
#Author: Student
#Date written: 25/8/2023
#Date tested and approved: 25/8/2023
# Revision History:

import getpass
from colorama import Fore

counter_upper =0#Upper
counter_lower =0#Lower
counter_digit =0#digits
counter_length =0#length

print(Fore.MAGENTA +'''$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n
\tWelcome to The Shadow Wizard Password Checker\n
\t\t\t -We love checking passwords-⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n''')

#user input will be obscured for privacy reasons + whitespace stripped
entered_password=getpass.getpass(Fore.WHITE + "What password you'd like to check?\n")
test_password=entered_password.rstrip()
#print(entered_password)

#Password length checker
counter_length =(len(test_password))
#Counting each required metric
for e in test_password:
  if(e.isupper()) is True:
    counter_upper += 1    
  elif(e.islower()) is True:
    counter_lower += 1  
  elif (e.isdigit()) is True:
    counter_digit += 1

#Print out password statistics, can be commented out to hide this info
print("Your password contains: ")
print("Uppercase -", counter_upper)
print("Lowercase -", counter_lower)
print("Digits -", counter_digit)
print("Length -", counter_length)

#Final results
if counter_upper <2 or counter_lower <2 or counter_digit <2 or counter_length <14 or counter_length >25:
  print(Fore.RED + "\nPassword is not strong enough - please revise")
else:
  print(Fore.GREEN + "\nPassword is strong enough.")