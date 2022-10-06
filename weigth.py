weight = float(input("Weight: "))
unit = input("(K)g or (L)bs").lower()
libres_constant = 2.20462262185

if unit == "k":
    print("Weight in K: ", weight)
elif unit == "l":
    print("Weight in L: ", weight * libres_constant)
else:
    print("Enter a valid unit")
