import random
quit = "n"
while quit == "n":
    print(f"Ohjelma jatkuu niin kauan, kuin vastaat {quit}")
    my_number = random.random() * 5 + 10
    print(f"Satunnaisluku 10-15 väliltä {my_number}")
    quit = input("Do you want to quit? ")
print(f"Silmukan suoritus loppui, kun vastasit {quit}")