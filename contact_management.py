
import json
import os

FILE_NAME = "contacts.json"


# Load contacts from JSON file
def load_contacts():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return []
    return []


# Save contacts to JSON file
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


# Add a new contact
def add_contact(contacts):
    print("\n--- Add New Contact ---")

    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    if not name or not phone or not email:
        print("All fields are required!")
        return

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    save_contacts(contacts)

    print("Contact added successfully!")


# View all contacts
def view_contacts(contacts):
    print("\n--- Contact List ---")

    if not contacts:
        print("No contacts found.")
        return

    for index, contact in enumerate(contacts, start=1):
        print(f"\nContact {index}")
        print("Name:", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])


# Edit an existing contact
def edit_contact(contacts):
    view_contacts(contacts)

    if not contacts:
        return

    try:
        number = int(input("\nEnter contact number to edit: "))

        if 1 <= number <= len(contacts):
            contact = contacts[number - 1]

            print("\nPress Enter to keep the existing value.")

            name = input(f"New name ({contact['name']}): ").strip()
            phone = input(f"New phone ({contact['phone']}): ").strip()
            email = input(f"New email ({contact['email']}): ").strip()

            if name:
                contact["name"] = name
            if phone:
                contact["phone"] = phone
            if email:
                contact["email"] = email

            save_contacts(contacts)
            print("Contact updated successfully!")

        else:
            print("Invalid contact number.")

    except ValueError:
        print("Please enter a valid number.")


# Delete a contact
def delete_contact(contacts):
    view_contacts(contacts)

    if not contacts:
        return

    try:
        number = int(input("\nEnter contact number to delete: "))

        if 1 <= number <= len(contacts):
            removed = contacts.pop(number - 1)
            save_contacts(contacts)

            print(removed["name"], "deleted successfully!")

        else:
            print("Invalid contact number.")

    except ValueError:
        print("Please enter a valid number.")


# Main program
def main():
    contacts = load_contacts()

    while True:
        print("\n================================")
        print("     CONTACT MANAGEMENT SYSTEM")
        print("================================")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            add_contact(contacts)

        elif choice == "2":
            view_contacts(contacts)

        elif choice == "3":
            edit_contact(contacts)

        elif choice == "4":
            delete_contact(contacts)

        elif choice == "5":
            print("\nThank you for using Contact Management System!")
            break

        else:
            print("Invalid choice! Please select 1 to 5.")


if __name__ == "__main__":
    main()
