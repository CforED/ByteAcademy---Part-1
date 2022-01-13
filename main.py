# Test our setup
print("This Worked")

example_variable = 12 # 12 is an integer

print(example_variable)

our_float = 12.0 # 12.0 is a float or a floating point number

# print(example_variable, our_float)

our_string = "this is a string" # this is a string
other_string = 'this is another string'

# Boolean values
first_bool = True
second_bool = False

# the None type
none_type = None

# print(none_type, second_bool)

# Mathematical operators:
addition = 12 + 9
subtraction = 12 - 9.0
multiplication = 12 * 9
division = 12 / 9
exponentiation = 12 ** 9

print(addition, subtraction, division)

# More division operators:
floor_or_integer_division = 37 // 2
modulus_division = 37 % 2

print(floor_or_integer_division, modulus_division)

print((4 + 3) * 2) # PEMDAS

a = 9
b = 90
print(a + b)

# Comparison operators:
greater_than = 3 > 2
less_than = 3 < 2
less_than_or_equal_to = 3 <= 2
greater_than_or_equal_to = 3 >= 2

print(greater_than, less_than)

equal_to = 3 == 3.0
not_equal_to = 3 != 3.0

print(equal_to) # True

print("string" != 'sTring') # True

# Concatenation operator:
example = "example"
concatenation = "this is " + example
repetition = "abc" * 4
print(concatenation, repetition)

our_int = 3
our_float = float(our_int)
print(our_float)

new_float = float("3.1")
print(new_float)
print(type(new_float))
# str() takes an input and converts it to a string
# int() converts its input to the integer type

# bool constructor:
print(bool(""))
# Things that return False:
# False, None, 0, 0.0, "", ''

lowered = "THIS IS UPPERCASE".lower() # this is a method
uppered = "this is lowercase".upper() # this is a method

print(lowered, uppered)

formatter = "This is a {}".format("string")
formatter_two = f"Lowered was: {lowered}"
print(formatter_two)

rounded = 12.771628947174
print(f"Rounded: {rounded: .1f}")

user_input = input("Here's our prompt: ")
print(user_input)
from replit import db
