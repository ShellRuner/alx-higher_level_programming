#!/usr/bin/python3
Square = __import__('6-square').Square

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")

my_square_3 = Square(0, (10,3))
#my_square_3.position = (0,3)
my_square_3.my_print()

print("--")

#my_square_3 = Square(3, (1,'3'))
#try:
#    my_square_3.position = (1, '3')
#except TypeError as e:
#    print(e)
#print("--")
#my_square_3.my_print()

