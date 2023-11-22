import os

path = "C:\\Users\\felip\\OneDrive\\Área de Trabalho"

if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("This is a file")
    elif os.path.isdir(path):
        print("This is a directory")
else:
    print("That location doesn't exist")

try:
    with open("test.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")
    