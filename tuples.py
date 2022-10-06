##Besides a normal array a tuple is created by
#assining them with ( ) and are inmutable#
numbers = (1,2,3,3)
num = (1)
# numbers[0] = 10 # This will output error aswell
print(numbers.count(2))
print(numbers.count(3))

print(numbers.index(1))
numbers.__add__(num)