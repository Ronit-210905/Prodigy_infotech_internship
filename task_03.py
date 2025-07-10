import json
import os

FILE_NAME = "contacts.json"

def load_contacts():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("✅ Contact added successfully!")

def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("📭 No contacts found.")
        return
    print("\n📇 Contact List:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']} - {contact['email']}")

def edit_contact():
    view_contacts()
    contacts = load_contacts()
    if not contacts:
        return
    try:
        index = int(input("Enter the contact number to edit: ")) - 1
        if 0 <= index < len(contacts):
            contacts[index]["name"] = input("New Name: ")
            contacts[index]["phone"] = input("New Phone: ")
            contacts[index]["email"] = input("New Email: ")
            save_contacts(contacts)
            print("✏️ Contact updated successfully!")
        else:
            print("❌ Invalid contact number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def delete_contact():
    view_contacts()
    contacts = load_contacts()
    if not contacts:
        return
    try:
        index = int(input("Enter the contact number to delete: ")) - 1
        if 0 <= index < len(contacts):
            contacts.pop(index)
            save_contacts(contacts)
            print("🗑️ Contact deleted successfully!")
        else:
            print("❌ Invalid contact number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def main():
    while True:
        print("\n📞 Contact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            edit_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select from 1 to 5.")

if __name__ == "__main__":
    main()
