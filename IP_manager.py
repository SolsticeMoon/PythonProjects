IP_list = ["192.105.50.1", "255.255.255.0"]
stale_IP = "Toad"
fresh_IP = "Frog"

def add_ip():
    new_IP = input("Please enter the IP address you wish to add\n")
    IP_list.append(new_IP)
    main()

def remove_ip():
    print(IP_list)
    deleted_IP = int(input("What number of the IP you'd like to remove?\n(1 for the first, 2 for the second etc.)\n"))
    IP_list.pop(deleted_IP - 1)
    main()

def replace_ip():
    action_counter = 0
    stale_IP = input("What IP would you like to replace?\n")
    fresh_IP = input("What IP would you like to put instead?\n")
    for e in range(len(IP_list)):
        if IP_list[e] == stale_IP:
            IP_list[e] = fresh_IP
            action_counter += 1
    print(f"{stale_IP} was replaced with {fresh_IP}, {action_counter} times.")
    main()

def show_list():
    print(f"The current list of IP addresses is\n{IP_list}")
    main()

def show_menu():
    print("OPTIONS ~\n1. Add a new IP address to your list\n2. Remove an existing IP address according to its position on the list\n3. Replace all instances of an existing IP address with a new one\n4. Show the current IP list\n5. Show this menu\n6. Exit the program")
    main()

def end_program():
    print("Goodbye")
    exit()

def main():

    
    choice = int(input("\nWhat would you like to do?\n(Enter a number between 1-6 to make your choice, press 5 for help)\n"))
    
    if choice == 1:
        add_ip()
    elif choice == 2:
        remove_ip()
    elif choice == 3:
        replace_ip()
    elif choice == 4:
        show_list()
    elif choice == 5:
        show_menu()
    else:
        end_program()

# Initial call to start the program
print('''$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n
\tWelcome to the Shadow Wizard IP Address Manager\n
\t\t ~-We love Managing IP Addresses-~

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n''')
main()

