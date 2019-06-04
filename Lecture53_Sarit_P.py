price = int(input("price :"))
def vatcalculator(price):
    result = price+(price*7/100)
    return result

print("Totalprice :",vatcalculator(price))