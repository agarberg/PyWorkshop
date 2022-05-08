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
# when we are looping, we only need a start and finish remember JS, let i =0(start) i>array.length (finish)
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