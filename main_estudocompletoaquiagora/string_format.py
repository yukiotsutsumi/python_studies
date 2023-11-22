# str.format() = optional method that gives users more control

animal = "dog"
item = "sun"

print("The {} jumped over the {}".format(animal,item))
print("The {1} jumped over the {0}".format(animal,item)) #positional argument

name = "Yukio"

print("Hello, my name is{}".format(name))
print("Hello, my name is {:10}. Nice tom meet you".format(name))
print("Hello, my name is {:<10}. Nice tom meet you".format(name))
print("Hello, my name is {:>10}. Nice tom meet you".format(name))
print("Hello, my name is {:^10}. Nice tom meet you".format(name))

pizinho: float = 3.1415
number = 1000

print("the number pi is {:.3f}".format(pizinho))
print("The number is {:,}".format(number))
print("The number is {:b}".format(number))
print("The number is {:o}".format(number))
print("The number is {:X}".format(number))
print("The number is {:E}".format(number))
