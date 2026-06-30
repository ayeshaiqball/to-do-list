user = 'random'

data = []

def show():
    print('Menu: ')
    print("1. Add an item in the list")
    print("2. Remove item from the list")
    print("3. View the list of items")
    print("4. Exit")

show()

while user != '4':
        

    user = input('enter your choice: ')

    if user == '1':
        item = input("Enter an item: ")
        data.append(item)
        print(f" Item Added : {item}")

    elif user== '2':
        item = input("Which item has to be removed? ")
        if item in data:
            data.remove(item)
            print(f"Removed items: {item}")
        else: 
            print("Item does not exist")

    elif user == '3':
        print("List of to do-list items: ")
        for item in data:
            print(item)

    elif user == '4':
        print("GoodBye")

    else:
        print("Please enter one of 1,2,3,4")

