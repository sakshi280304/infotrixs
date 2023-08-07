import json

CONTACTS_FILE = "contacts.json"


def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f)


def display_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("Contacts:")
        for index, contact in enumerate(contacts):
            print(f"{index + 1}. {contact['name']} - {contact['phone']}")


def add_contact(contacts, name, phone):
    contacts.append({"name": name, "phone": phone})
    save_contacts(contacts)
    print(f"Contact '{name}' with phone number '{phone}' added successfully!")


def remove_contact(contacts, index):
    if 0 < index <= len(contacts):
        contact_name = contacts[index - 1]["name"]
        del contacts[index - 1]
        save_contacts(contacts)
        print(f"Contact '{contact_name}' removed successfully!")
    else:
        print("Invalid contact index.")


def main():
    contacts = load_contacts()

    while True:
        print("\n--- Contact Management System ---")
        print("1. Display Contacts")
        print("2. Add Contact")
        print("3. Remove Contact")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            display_contacts(contacts)
        elif choice == "2":
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            add_contact(contacts, name, phone)
        elif choice == "3":
            display_contacts(contacts)
            index = int(input("Enter the index of the contact to remove: "))
            remove_contact(contacts, index)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
