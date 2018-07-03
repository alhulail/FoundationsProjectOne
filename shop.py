####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = ("Hadeel")
signature_flavors = ["Rainbow", "Volcano", "Monster"]
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    # your code goes here!
    print("MENU")
    for item in menu:
        print("- %s KD %s" %(item, menu[item]))


def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    # your code goes here!
    for original_flavor in original_flavors:
        print(original_flavor)


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    # your code goes here!
    for signature_flavor in signature_flavors:
        print (signature_flavor)


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    # your code goes here!
    if order in  signature_flavors:
        return True
    elif order in original_flavors:
        return True
    elif order in menu:
        return True
    else:
        return False



def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    # your code goes here!
    user_input = input("What would you like to order \n")

    while user_input.lower() != "Exit":
        if is_valid_order(user_input):
            order_list.append(user_input)
        else:
            print("order is not valid")
        user_input = input("Anything else?")

    return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here!
    if total >= 5:
        return True
    else:
        return False


def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    # your code goes here!
    for order in order_list:
        if order in original_flavors:
            total += 2
        elif order in signature_flavors:
            total += signature_price
        elif order in menu:
            if order == "tea":
                total += 0.900
            elif order == "coffe":
                total += 1.00
            elif order == "bottled water":
                total += 0.750

    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    for order in order_list:
        print(order_list)
    # your code goes here!
