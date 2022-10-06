## function declaration
def greet(first_name, last_name):
    print("Hello there", first_name)
    print("Welcome aboard", last_name)

#parameters
greet("Mosh", "Hamedani")
greet("Jhon", "smith")

#optional parameters
#

def get_greeting(name):
    return f"Hi {name}"

message = get_greeting("holi")
file = open("content.txt", "w")
file.write(message)

def return_greet(name):
    return (f"hi {name}")

print(return_greet("Mosh"))