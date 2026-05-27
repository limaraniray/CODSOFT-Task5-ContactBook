"""
CODSOFT Python Internship - Task 5
Contact Book Application
"""

contacts = {}  # { phone_number: {name, phone, email, address} }

def show_menu():
    print("\n" + "="*45)
    print("         📒 CONTACT BOOK APP")
    print("="*45)
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    print("="*45)

def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Name:         ").strip()
    if not name:
        print("❌ Name is required.")
        return

    phone = input("Phone Number: ").strip()
    if not phone:
        print("❌ Phone number is required.")
        return

    if phone in contacts:
        print(f"❌ A contact with phone '{phone}' already exists.")
        return

    email   = input("Email:        ").strip()
    address = input("Address:      ").strip()

    contacts[phone] = {
        "name":    name,
        "phone":   phone,
        "email":   email,
        "address": address,
    }
    print(f"✅ Contact '{name}' added successfully!")

def view_contacts():
    if not contacts:
        print("📭 No contacts found. Add some first!")
        return
    print(f"\n--- All Contacts ({len(contacts)}) ---")
    print(f"{'#':<4} {'Name':<20} {'Phone':<15}")
    print("-" * 40)
    for i, c in enumerate(contacts.values(), 1):
        print(f"{i:<4} {c['name']:<20} {c['phone']:<15}")

def display_contact(c):
    print("\n  ┌─────────────────────────────")
    print(f"  │  👤 Name:    {c['name']}")
    print(f"  │  📞 Phone:   {c['phone']}")
    print(f"  │  📧 Email:   {c['email'] or 'N/A'}")
    print(f"  │  🏠 Address: {c['address'] or 'N/A'}")
    print("  └─────────────────────────────")

def search_contact():
    if not contacts:
        print("📭 No contacts to search.")
        return
    query = input("Search by name or phone: ").strip().lower()
    if not query:
        print("❌ Search term cannot be empty.")
        return

    results = [c for c in contacts.values()
               if query in c["name"].lower() or query in c["phone"]]

    if results:
        print(f"\n🔍 Found {len(results)} result(s):")
        for c in results:
            display_contact(c)
    else:
        print("❌ No contacts found matching your search.")

def update_contact():
    view_contacts()
    if not contacts:
        return
    phone = input("Enter phone number of contact to update: ").strip()
    if phone not in contacts:
        print("❌ Contact not found.")
        return

    c = contacts[phone]
    print(f"\nUpdating: {c['name']} — leave blank to keep current value.")

    new_name    = input(f"Name [{c['name']}]: ").strip()
    new_phone   = input(f"Phone [{c['phone']}]: ").strip()
    new_email   = input(f"Email [{c['email']}]: ").strip()
    new_address = input(f"Address [{c['address']}]: ").strip()

    if new_name:    c["name"]    = new_name
    if new_email:   c["email"]   = new_email
    if new_address: c["address"] = new_address

    if new_phone and new_phone != phone:
        if new_phone in contacts:
            print(f"❌ Phone '{new_phone}' already used by another contact.")
        else:
            contacts[new_phone] = c
            contacts[new_phone]["phone"] = new_phone
            del contacts[phone]
            print(f"✅ Contact updated and phone changed to '{new_phone}'!")
            return

    print(f"✅ Contact '{c['name']}' updated successfully!")

def delete_contact():
    view_contacts()
    if not contacts:
        return
    phone = input("Enter phone number of contact to delete: ").strip()
    if phone not in contacts:
        print("❌ Contact not found.")
        return
    name = contacts[phone]["name"]
    confirm = input(f"Are you sure you want to delete '{name}'? (y/n): ").strip().lower()
    if confirm == "y":
        del contacts[phone]
        print(f"🗑️ Contact '{name}' deleted!")
    else:
        print("❎ Deletion cancelled.")

def main():
    print("Welcome to the Contact Book App!")
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select 1-6.")

if __name__ == "__main__":
    main()