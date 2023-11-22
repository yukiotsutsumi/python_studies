# scope = the region that a variable is recognized, is only avaiable from inside the region
# *args = parameter that will pack all arguments into a tuple
# kwargs = parameter that will pack all arguments into a dictionary

def display_name():
    name = "yukio"  # só existe dentro dessa função
    print(name)


# print(name) -> vai dar erro!

def add(*stuff):
    sum = 0
    stuff = list(stuff)  # transforma uma tuple numa lista!!!
    stuff[0] = 0
    for i in stuff:
        sum += i
    return sum


print(add(1, 2, 3, 4, 5, 6, 7, 8))


def hello(**kwargs):
    # print("Hello ", kwargs['first'] + " " + kwargs['last'])
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")


hello(title="Mrs.", first="Yukio", middle="blabla", last="Tsutsumi")
