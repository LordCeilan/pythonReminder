temperature = 12

if temperature > 30:
    print("It's a fucking hot day")
    print("Drink plenty of water")
elif temperature > 20: #(20, 30]
    print("It's a nice day")
elif temperature > 10: #(10, 20] not includes 20
    print("It's a bit cold")
else:
    print("It's Hella cold today")


print("done")


