Inventory=[]
def addItem():
    name=input('Please enter name of item: ')
    quantity=int(input('Please enter quantity of item: '))
    price=float(input('Please enter price of item: '))
    item={name:{'quantity':quantity,'price':price}}
    Inventory.append(item)
def update_quantity(dict,name,quantity):
    for item in dict:
        for Product, details in item.items():
            if Product==name:
                for key, value in details.items():
                    if key=='quantity': details[key]=quantity

def viewItems(dict):
    for item in dict:
        for Product,details in item.items():
            print(f'\n{Product}: ')
            for key,value in details.items():
                print(f'\t\t{key}: {value}')
def TotalValue(dict):
    total=0
    for item in dict:
        for Product,details in item.items():
            total+=float(details['quantity'])*details['price']
    return total



while True:
    prompt=("\nPlease enter a number (1-5):\n1-Add Item\n2-view Items\n3-update quantity\n"
            "4-Total Value of Inventory\n5-To exit\n")
    choice=int(input(prompt))
    if choice==1:
        addItem()
    elif choice==2:
        viewItems(Inventory)
    elif choice==3:
        name=input('Please Enter name of Product: ')
        quantity=input('Please Enter quantity: ')
        update_quantity(Inventory, name,quantity)
    elif choice==4:
        print(TotalValue(Inventory))
    elif choice==5:
        break
