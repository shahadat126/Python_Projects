import csv
import os



class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def to_list(self):
        return [self.name, self.phone, self.email, self.address]

class ContactBook:
    def __init__(self, filename='contacts.csv'):
        self.filename = filename
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        print("Loading contacts from contacts.csv...", end="")
        if os.path.exists(self.filename):
            with open(self.filename, 'r', newline='') as file:
                reader = csv.reader(file)
                self.contacts = [Contact(*row) for row in reader]
        print(" Done!")

    def save_all(self):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for c in self.contacts:
                writer.writerow(c.to_list())

    def add_contact(self, contact):
        for c in self.contacts:
            if c.phone == contact.phone:
                print("Error: Phone number already exists for another contact.")
                return
        self.contacts.append(contact)
        with open(self.filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(contact.to_list())
        print("Contact added successfully!")

    def view_contacts(self):
        print("===== All Contacts =====")
        print(f"DEBUG: Total contacts: {len(self.contacts)}")  # Debug line

        if not self.contacts:
            print("No contacts found.")
        for i, c in enumerate(self.contacts, start=1):
            print(f"\n{i}. Name : {c.name}\nPhone : {c.phone}\nEmail : {c.email}\nAddress: {c.address}")
        print("========================")

    def search_contact(self, term):
        found = False
        for c in self.contacts:
            if term.lower() in c.name.lower() or term in c.phone or term.lower() in c.email.lower():
                print("\nSearch Result:")
                print(f"Name : {c.name}\nPhone : {c.phone}\nEmail : {c.email}\nAddress: {c.address}")
                found = True
                break
        if not found:
            print("No matching contact found.")

    def delete_contact(self, phone):
        for i, c in enumerate(self.contacts):
            if c.phone == phone:
                confirm = input(f"Are you sure you want to delete contact number {phone}? (y/n): ")
                if confirm.lower() == 'y':
                    del self.contacts[i]
                    self.save_all()
                    print("Contact deleted successfully!")
                else:
                    print("Deletion canceled.")
                return
        print("No contact found with that phone number.")

# CLI Starts Here
def main():
    print("Welcome to the Contact Book CLI System!\n")
    contact_book = ContactBook()

    while True:
        print("""
=========== MENU ===========
1. Add Contact
2. View Contacts
3. Search Contact
4. Remove Contact
5. Exit
============================
""")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            name = input("Enter Name: ")
            phone = input("Enter Phone Number: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            contact = Contact(name, phone, email, address)
            contact_book.add_contact(contact)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            term = input("Enter search term (name/email/phone): ")
            contact_book.search_contact(term)

        elif choice == '4':
            phone = input("Enter the phone number of the contact to delete: ")
            contact_book.delete_contact(phone)

        elif choice == '5':
            print("Thank you for using the Contact Book CLI System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
