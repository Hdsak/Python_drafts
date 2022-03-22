def restaurant():
    menu = {'sandwich': 10, 'tea': 7, 'salad': 9}
    price = 0
    while True:
        order = input("Order: ")
        if not order:
            break
        if order in menu.keys():
            price += menu[order]
            print("{} costs {}, total is {}".format(order, menu[order], price))
        else:
            print("We are out of {}".format(order))


restaurant()