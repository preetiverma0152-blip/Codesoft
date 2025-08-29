# Contact Book Application in Python

contacts = []  # List to store all contacts


# Function to add a contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    print("✅ Contact added successfully!\n")


# Function to view all contacts
def view_contacts():
    if not contacts:
        print("No contacts found!\n")
        return
    print("\n---- Contact List ----")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")
    print()


# Function to search for a contact
def search_contact():
    keyword = input("Enter name or phone number to search: ")
    found = False
    for contact in contacts:
        if contact['name'] == keyword or contact['phone'] == keyword:
            print("\n---- Contact Found ----")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}\n")
            found = True
    if not found:
        print("❌ No contact found.\n")


# Function to update a contact
def update_contact():
    name = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if contact['name'] == name:
            print("Enter new details (leave blank to keep old):")
            new_phone = input("New phone: ") or contact['phone']
            new_email = input("New email: ") or contact['email']
            new_address = input("New address: ") or contact['address']

            contact['phone'] = new_phone
            contact['email'] = new_email
            contact['address'] = new_address
            print("✅ Contact updated successfully!\n")
            return
    print("❌ Contact not found.\n")


# Function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)
            print("✅ Contact deleted successfully!\n")
            return
    print("❌ Contact not found.\n")


# Main program loop
def contact_book():
    while True:
        print("---- Contact Book ----")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("👋 Exiting Contact Book. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please try again.\n")


# Run the program
contact_book()
