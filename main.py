import time
import os  # for file

# prices hard coded cuz env hard
espresso_p = 60
latte_p = 80
capp_p = 70
caramel_p = 90
small_f = 1.0
med_f = 1.3
large_f = 1.6
sugar_p = 5  

prep_t = 30  # seconds
order_f = "orders.txt"  # file name

# menu dict
menu = {
    "1": {"name": "Espresso", "price": espresso_p},
    "2": {"name": "Latte", "price": latte_p},
    "3": {"name": "Cappuccino", "price": capp_p},
    "4": {"name": "Caramel Macchiato", "price": caramel_p}
}

# sizes
sizes = {
    "1": {"name": "Small", "factor": small_f},
    "2": {"name": "Medium", "factor": med_f},
    "3": {"name": "Large", "factor": large_f}
}

# functions

def coffee_choice():  # get coffee
    print("\nCoffee menu:")
    for k in menu:
        i = menu[k]
        print(k + ". " + i["name"] + " - " + str(i["price"]) + " Toman")  # print menu
    ch = input("Pick number: ")
    if ch not in menu:  # check
        print("Wrong, espresso it is")
        ch = "1"
    return ch

def size_choice():  # size
    print("\nSize:")
    for k in sizes:
        i = sizes[k]
        print(k + ". " + i["name"] + " x" + str(i["factor"]))
    ch = input("Pick: ")
    if ch not in sizes:
        print("Small default")
        ch = "1"
    return ch

def sugar_choice():  # sugar or not
    print("\n1. Sugar +5 Toman")
    print("2. No sugar")
    ch = input("1 or 2? ")
    if ch == "1":
        return True  # has sugar
    else:
        return False

def wait_time(s):  # countdown simple
    print("\nPreparing...")
    for x in range(s, 0, -1):
        print(str(x) + " seconds...", end="\r")  # no fancy r
        time.sleep(1)
    print("Ready! Enjoy")

def write_order(d):  # save to file
    f = open(order_f, "a")  # open append
    f.write(d + "\n")
    f.close()  # close manual

def do_pay(tot):  # payment fake
    print("\nPay: " + str(tot) + " Toman")
    ok = input("Yes? y/n: ")
    if ok == "y":
        print("Paying..")
        time.sleep(2)
        print("Paid ok")
        return True
    else:
        print("No pay")
        return False

# main part
print("Welcome Coffee Shop!")  # start

total = 0  # total price
order_list = []  # list of orders

while True:  # loop for orders
    c = coffee_choice()  # get coffee
    s = size_choice()  # size
    sug = sugar_choice()  # sugar

    # calc price
    cof = menu[c]  # coffee info
    sz = sizes[s]  # size info
    price = cof["price"] * sz["factor"]  # base * factor
    if sug == True:  # add sugar
        price = price + sugar_p

    total = total + price  # add to total

    # make summary
    if sug:
        add_t = "with sugar"
    else:
        add_t = "no sugar"
    summ = cof["name"] + " (" + sz["name"] + ", " + add_t + ") - " + str(int(price)) + " Toman"
    order_list.append(summ)  # add to list

    more = input("\nAnother? y/n: ")
    if more != "y":  # stop
        break

# show order
print("\nOrder:")
for item in order_list:
    print("- " + item)
print("Grand total: " + str(int(total)) + " Toman")

# pay
if do_pay(total):
    wait_time(prep_t)  # prepare
    full_order = ", ".join(order_list) + " | Total: " + str(int(total)) + " Toman"
    write_order(full_order)  # save
    print("Order saved in file")

print("Bye! Come again")  # end
