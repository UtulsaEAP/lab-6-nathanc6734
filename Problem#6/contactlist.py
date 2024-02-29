'''
Name: Nathan Carr
Lab Time: Thursday @ 2pm
'''
def process_user_contacts(user_input):
    user_contacts = user_input.split()
    Dictionary = {}
    # Put word pairs into a dictionary
    for x in range(len(user_contacts)):
        Dictionary[user_contacts[x].split(",")[0]] = user_contacts[x].split(",")[1]

    # Get contact name from input, output contact's phone number
    contact_name = input("Enter the contact name: ")

    if contact_name in Dictionary:
        print(Dictionary[contact_name])
    else:
        print("Contact not found.")
    
if __name__ == '__main__':
    # Get input for word pairs
    user_input = input("Enter word pairs (name, phone number): ")

    # Call the function to process user contacts
    process_user_contacts(user_input)
