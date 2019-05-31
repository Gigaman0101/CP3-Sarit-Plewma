print("----------MUFU shop----------")
print("--sign in --")
usernameinput = input("username : ")
passwordinput = input("password : ")
if usernameinput == "INWZA007" and passwordinput == "12345":
    print("--------Welcome to MUFU shop--------")
    print("1. Pineapple  x1 :",23,"THB")
    print("2. Apple      x1 :",30,"THB")
    print("3. Orange     x1 :",15,"THB")
    print("4. Banana     x1 :",9,"THB")
    print("5. Watermelon x1 :",44,"THB")
    print("------------------------------------")
    Demand = input("Please choose your fruit :")
    if Demand == "Pineapple" :
        pricepine = 23
        p1 = int(input("How many product do you want ? =>"))
        sum1 = p1 * pricepine
        print("Total  :",sum1,"THB")
    elif Demand == "Apple" :
        priceApp = 30
        p2 = int(input("How many product do you want ? =>"))
        sum2 = p2 * priceApp
        print("Total  :",sum2,"THB")
    elif Demand == "Orange" :
        priceOr = 15
        p3 = int(input("How many product do you want ? =>"))
        sum3 = p3 * priceOr
        print("Total  :",sum3,"THB")
    elif Demand == "Banana " :
        priceBa = 9
        p4 = int(input("How many product do you want ? =>"))
        sum4 = p4 * priceBa
        print("Total  :",sum4,"THB")
    elif Demand == "Watermelon " :
        priceWa = 44
        p5 = int(input("How many product do you want ? =>"))
        sum5 = p5 * priceWa
        print("Total  :",sum5,"THB")
else :
    print("***Your username and password are not correct***")
