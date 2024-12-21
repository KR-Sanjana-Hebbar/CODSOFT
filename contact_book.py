class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}\nAddress: {self.address}\n"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        self.contacts.append(Contact(name, phone, email, address))
        print("Contact added successfully!\n")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts to display.\n")
        else:
            print("Contact List:")
            for index, contact in enumerate(self.contacts, start=1):
                print(f"{index}. {contact.name} - {contact.phone} - {contact.email} - {contact.address}")
            print()

    def search_contact(self):
        query = input("Enter contact name or phone number to search: ")
        results = [contact for contact in self.contacts if query.lower() in contact.name.lower() or query in contact.phone]
        if results:
            print("Search Results:")
            for contact in results:
                print(contact)
        else:
            print("No matching contacts found.\n")

    def update_contact(self):
        query = input("Enter name or phone number of the contact to update: ")
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone:
                print("Current details:")
                print(contact)
                contact.name = input("Enter new name (or press Enter to keep current): ") or contact.name
                contact.phone = input("Enter new phone number (or press Enter to keep current): ") or contact.phone
                contact.email = input("Enter new email (or press Enter to keep current): ") or contact.email
                contact.address = input("Enter new address (or press Enter to keep current): ") or contact.address
                print("Contact updated successfully!\n")
                return
        print("Contact not found.\n")

    def delete_contact(self):
        query = input("Enter name or phone number of the contact to delete: ")
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone:
                self.contacts.remove(contact)
                print("Contact deleted successfully!\n")
                return
        print("Contact not found.\n")

    def menu(self):
        while True:
            print("""
Contact Book Menu:
1. Add Contact
2. View Contact List
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
            """)
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                self.search_contact()
            elif choice == '4':
                self.update_contact()
            elif choice == '5':
                self.delete_contact()
            elif choice == '6':
                print("Exiting Contact Book. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    contact_book = ContactBook()
    contact_book.menu()
