"""A simple JSON-backed contact book."""

import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("contacts.json")


def load_contacts():
    return json.loads(DATA_FILE.read_text()) if DATA_FILE.exists() else []


def save_contacts(contacts):
    DATA_FILE.write_text(json.dumps(contacts, indent=2))


def main():
    contacts = load_contacts()
    while True:
        print("\n1) List  2) Add  3) Find  4) Delete  5) Quit")
        choice = input("Choose: ").strip()
        if choice == "1":
            for contact in contacts:
                print(f"{contact['name']}: {contact['phone']}")
        elif choice == "2":
            name = input("Name: ").strip()
            phone = input("Phone: ").strip()
            if name and phone:
                contacts.append({"name": name, "phone": phone})
                save_contacts(contacts)
        elif choice == "3":
            query = input("Search name: ").strip().lower()
            matches = [c for c in contacts if query in c["name"].lower()]
            print(*[f"{c['name']}: {c['phone']}" for c in matches], sep="\n")
        elif choice == "4":
            name = input("Exact name to delete: ").strip().lower()
            contacts = [c for c in contacts if c["name"].lower() != name]
            save_contacts(contacts)
        elif choice == "5":
            return
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
