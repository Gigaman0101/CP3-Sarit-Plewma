def login():
    username = input("username  :")
    password = input("password  :")
    if username == "KFC" and password == "12345":
        return showMenu()
    else:
        return False
def showMenu():
    print("----Ishop----")
    print("1. Vat calculator")
    print("2. Price calculator")
    menuSelect()
def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        print("Vat value :",vatCalculate(int(input("Input product price : "))))
    elif userSelected == 2:
        print("Total pricr :",priceCalculate())
    return userSelected
def vatCalculate(totalprice):
    vat = 7
    result = totalprice + (totalprice * vat / 100)
    return result
def priceCalculate():
    price1 = int(input("First product price : "))
    price2 = int(input("Second product price : "))
    return vatCalculate(price1 + price2)

login()