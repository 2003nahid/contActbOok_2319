def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")

    # Append contact to file
    with open("contacts.txt", "a") as file:
        file.write(f"{name},{phone},{email}\n")

    print("Contact added successfully!\n")


# Function to view all contacts
def view_contacts():
    try:
        with open("contacts.txt", "r") as file:
            contents = file.readlines()

        if len(contents) == 0:
            print("No contacts found.\n")
        else:
            print("\n--- All Contacts ---")
            for line in contents:
                name, phone, email = line.strip().split(",")
                print(f"Name: {name}, Phone: {phone}, Email: {email}")
            print()

    except FileNotFoundError:
        print("No contacts file found. Add a contact first.\n")


# Function to search contacts by name
def search_contact():
    search_name = input("Enter the name to search: ").lower()

    found = False

    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                name, phone, email = line.strip().split(",")
                if name.lower() == search_name:
                    print("\nContact Found:")
                    print(f"Name: {name}, Phone: {phone}, Email: {email}\n")
                    found = True
                    break

        if not found:
            print("No contact found with that name.\n")

    except FileNotFoundError:
        print("No contacts file found. Add a contact first.\n")


# Main program loop
while True:
    print("----- CONTACT BOOK -----")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        print("Exiting Contact Book... Bye!")
        break
    else:
        print("Invalid choice. Try again.\n")

