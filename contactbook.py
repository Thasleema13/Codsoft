#contact book

contacts = []

def add_contact():
  global contacts
  contact_id = len(contacts) + 1
  name = input("Enter contact name: ")
  phone = input("Enter phone number: ")
  contacts.append({"id": contact_id, "name": name, "phone": phone})
  print(f"Contact '{name}' added successfully.")

def view_contacts():
  if not contacts:
    print("No contacts found.")
  else:
    print("Contact List:")
    for contact in contacts:
      print(f"{contact['id']}. {contact['name']} - {contact['phone']}")

def search_contact():
  name = input("Enter name: ")
  results = [contact for contact in contacts if name.lower() in contact['name'].lower()] 
  if results:
    print("Search Results:")
    for contact in results:
      print(f"{contact['name']} - {contact['phone']}") 
  else:
    print("No contacts found.")

def update_contact():
  try:
    name =input("Enter contact name to update: ")
    for contact in contacts:
      if contact['name'].lower() == name.lower(): 
        new_name = input(f"Enter new name (current: {contact['name']}): ") 
        new_phone = input(f"Enter new phone number (current: {contact['phone']}): ") 
        contact['name'] = new_name
        contact['phone'] = new_phone
        print(f"Contact {name} updated successfully.")
        return
    print("Contact name not found.")
  except ValueError:
    print("Invalid input .")

def delete_contact():
  try:
    name = input("Enter contact name to delete: ") 
    for i, contact in enumerate(contacts):
      if contact['name'].lower() == name.lower():
        del contacts[i]
        print(f"Contact {name} deleted successfully.")
        return
    print("contact name not found.")
  except ValueError:
    print("Invalid input.")

while True:
  print("Contact book")
  print("1. Add Contact")
  print("2. View Contacts")
  print("3. Search Contacts")
  print("4. Update Contact")
  print("5. Delete Contact")
  print("6. Exit")
  choice = input("Enter your choice1/2/3/4/5/6): ")

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
    print("Exiting...")
    break
  else:
    print("Invalid choice.")
