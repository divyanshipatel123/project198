customerInLine = True
while customerInLine:
    total = 0
    print("####### For the billing process kindly fill the following details ########")
    name = input("Enter your name: ")
    add_item = True
    while add_item:
        print("#### Enter the number and quantity of items #####")
        quantity = float(input('Enter the price of items  : '))
        items = float(input("Enter the number of items  :"))
        total += quantity*items
        repeat = input("Do you want to add more items (Y/y , N/n): ")
        if repeat == "n" or repeat == "N":
            print("_"*50)
            print("Name :", name )
            print("Total :" , total )
            print()
            print("****Thankyou for shopping with us*****")
            print("_"*50)
            break
    new_customer = input("Go to the next person (Y/y , N/n)?")
    if new_customer=="N" or new_customer=="n":
        break
