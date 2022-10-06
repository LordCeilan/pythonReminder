## required parammeters should be declared before the optional ones
def increment(number, by=2):
    return number + by

print(increment(1, 7))


[2,3,4,5]

def multiply(*numbers): #(x,y)
    print(numbers)
    total= 1
    for number in numbers:
        print(number)
        # total = total * number
        total *= number
    return total


multiply(2,3,4,5)
## you can pass multiple key value pairs
##authomaticaly passes them
def save_user(**user):
    print(user["name"])

save_user(id = 1, name = "jhon", age=22)
