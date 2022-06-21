'''Simulates a telephone book; you can create, delete, update and insert new contacts'''

def main():
    print("---------------WELCOME------------------------")
    print()
    while True:
        print("1 - Create telephone book")
        print("2 - Insert contact")
        print("3 - Delete contact")
        print("4 - Update contact")
        print("5 - List contacts")
        print("6 - Exit")
        option = int(input("Option: "))
        print()
        if option == 1:
            calendar = createTelephoneBook()
        elif option == 2:
            insertContact(calendar)
        elif option == 3:
            name = input("Name of the contact: ")
            deleteContact(calendar,name)
        elif option == 4:
            name = input("Name of the contact: ")
            updateContact(calendar,name)
        elif option == 5:
            listContacts(calendar)
        else:
            break
        input()

def createTelephoneBook():
    calendar = {}
    print("Telphone Book was created")
    return calendar

def insertContact(calendar):
    name = input("Name: ")
    phone = input("Number")
    calendar[name] = phone
    print("New number inserted")

def deleteContact(calendar,name):
    del calendar[name]
    print("Contact deleted")

def updateContact(calendar,name):
    phone = input("New number: ")
    calendar[name] = phone
    print("Number updated")

def listContacts(calendar):
    for i in calendar.keys():
        print(i, "=", calendar[i])

main()