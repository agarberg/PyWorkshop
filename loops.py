import enum


animals = ["dog", "cat", "iguana","bat"]
for animal in animals:
    print(f"the animal is: {animal}")
# Printed:
# the animal is: dog
# the animal is: cat
# the animal is: iguana
# the animal is: bat
print("outside of the loop", animal)
# last animal is shown outside of the loop-- (outside of the loop bat) this is due to being "out of scope"
range(3)
        # range(0, 3)
# range is used to loop over - it saves the first and last number - and not the middle numbers to save space 
# when we are looping, we only need a start and finish just like JS, let i =0(start) i>array.length (finish)
list(range(3))
        # [0, 1, 2]
list(range(6,7))
        # [6]
list(range(6,10))
        # [6, 7, 8, 9]

for num in range (3, 10):
    print(num) 
# 3 , 4, 5, 6, 7, 8, ,9 
enumerate(animals)
# <enumerate object at 0x105ec4200>
list(enumerate(animals))
# [(0, 'dog'), (1, 'cat'), (2, 'iguana'), (3, 'bat')]
animals
# ['dog', 'cat', 'iguana', 'bat']

for index, animal in enumerate(animals):
    print(f"{index} animal at {animal}")
        # 0 animal at dog
        # 1 animal at cat
        # 2 animal at iguana
        # 3 animal at bat

hex_colors = {
    "Red": "#FF0000",
    "Green": "#008000",
    "Blue": "#0000FF",
}
for color in hex_colors:
    print(color)
# Red
# Green
# Blue

hex_colors.items()
# dict_items([('Red', '#FF0000'), ('Green', '#008000'), ('Blue', '#0000FF')])
#  returns a list of tupils - key/values

for key, values in hex_colors.items():
    print(key)
    print("...")
    print(values)
# Red
# ...
# #FF0000
# Green
# ...
# #008000
# Blue
# ...
# #0000FF

# while loop -- make sure it will break out!!!
val = 0
while val < 5:
    print(val)
    val+=1
    0
# 1
# 2
# 3
# 4

names = ["Adam", "John", "Colie", "Nick"]
def return_target(target="Adam"):
    for name in names:
        if name == target:
            return name 
return_target()
# 'Adam'

# BREAK

