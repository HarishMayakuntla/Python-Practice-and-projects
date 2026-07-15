## ================= shoping cart ===============
# here we use some methods in list
# append()
# and remove()
# and clear()



cart = []

while True:
    print("\n1.Add Item")
    print("2.Remove Item")
    print("3.View Cart")
    print("4.Clear Cart")
    print("5.Exit")

    choice = int(input("Choice: "))

    if choice == 1:
        item = input("Item: ")
        cart.append(item)

    elif choice == 2:
        item = input("Remove: ")
        if item in cart:
            cart.remove(item)

    elif choice == 3:
        print(cart)

    elif choice == 4:
        cart.clear()

    else:
        break





    # 1.Add Item
    # 2.Remove Item
    # 3.View Cart
    # 4.Clear Cart
    # 5.Exit
    # Choice: 1 
    # Item: masala

    # 1.Add Item
    # 2.Remove Item
    # 3.View Cart
    # 4.Clear Cart
    # 5.Exit
    # Choice: 3
    # ['masala']

    # 1.Add Item
    # 2.Remove Item
    # 3.View Cart
    # 4.Clear Cart
    # 5.Exit
    # Choice: 1
    # Item: ginger

    # 1.Add Item
    # 2.Remove Item
    # 3.View Cart
    # 4.Clear Cart
    # 5.Exit
    # Choice: 1
    # Item: coriander

    # 1.Add Item
    # 2.Remove Item
    # 3.View Cart
    # 4.Clear Cart
    # 5.Exit
    # Choice: 3
    # ['masala', 'ginger', 'coriander']

    # 1.Add Item
    # 2.Remove Item
    # 3.View Cart
    # 4.Clear Cart
    # 5.Exit
    # Choice: 2
    # Remove: ginger

    # 1.Add Item
    # 2.Remove Item
    # 3.View Cart
    # 4.Clear Cart
    # 5.Exit
    # Choice: 3
    # ['masala', 'coriander']

    # 1.Add Item
    # 2.Remove Item
    # 3.View Cart
    # 4.Clear Cart
    # 5.Exit
    # Choice: 5
     

     