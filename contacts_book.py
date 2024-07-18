contacts = []
def add_contact():
  name = input("Enter contact name: ")
  phone_number = input("Enter phone number: ")
  email = input("Enter email (optional): ")
  contact = {"name": name, "phone_number": phone_number, "email": email}
  contacts.append(contact)
  print("Contact added successfully!")

def view_contacts():
  if not contacts:
    print("There are no contacts saved yet.")
    return
  print("\nContact List:")
  for i, contact in enumerate(contacts):
    print(f"{i+1}. {contact['name']} - {contact['phone_number']}")

def search_contact():
  search_term = input("Enter name to search: ")
  found = False
  for contact in contacts:
    if search_term.lower() in contact["name"].lower():
      print(f"\nContact Found:")
      print(f"Name: {contact['name']}")
      print(f"Phone Number: {contact['phone_number']}")
      if contact["email"]:
        print(f"Email: {contact['email']}")
      found = True
      break
  if not found:
    print("Contact not found.")

def main_menu():
  while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
      add_contact()
    elif choice == '2':
      view_contacts()
    elif choice == '3':
      search_contact()
    elif choice == '4':
      print("Exiting...")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main_menu()
