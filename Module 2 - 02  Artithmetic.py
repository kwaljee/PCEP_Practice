# Operators


# # Asterisk
# print(2*3) # multiplication
# print(2**3) # exponential multiplication
#
# # Slash
# print()
# print(6/2, " One slash division with float output")
# print(6/4, " One slash division with float output in decimals no rounding")
# print(6//2, "   Two slash division with no float output rounded values")
# print(6//5, "   Two slash division with no float output rounded values")
# print(6.0//4, " Two slash rounded with decimals because numerator value in decmial format")
# print(11//4.0, " Two slash rounded with decimals because denominator value provides float")
# print(4.3//2, "neareset decimal")
#
#
# # Percent symbol (modulo operator)
# print()
# print (6%3, "modulo operator remainder whereby output is 0")
# print (6%4, "modulo operator remainder whereby output is 2")
# print(12 % 4.5)
#
# #Right sided binding example
# print()
# print(2 ** 2 ** 3)
#
# # Examples
# print()
# print((5 * ((25 % 13) + 100) / (2 * 13)) // 2) # output is 10.0
# print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4)) # -0.5 0.5 0 -1
# print((2 % -4), (2 % 4), (2 ** 3 ** 2)) # -2 2 512
# print(25.0**0.5)
#
#
#
# # Kilometers and Miles Converter
#
# #kilometers = 12.25
# #miles = 7.38
#
# #kilometers = float(input("Enter kilometers: "))
# #miles = float(input("Enter miles: "))
#
#
# #miles_to_kilometers = miles * 1.61
# kilometers_to_miles = kilometers/1.61
#
# #print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
# #print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

# # Order of Operations
# a = 6
# b = 3
# a //= 2 * b # // will return integer division
# print(a)
#
# a = 6
# b = 3
# a /= 2 * b # / will return a floating point
# print(a)

# Exercise
#x = float(input("Enter value for x: "))
#y = 1/(x+1/(x+1/(x+1/x))) #input: 1, expected output: 0.6000000000000001
#print("y =", y)

x = 1/2+3//3+4**2

x1 = 4**2
x2 = 3//3
x3 = 1/2

y = x1 + x2 + x3


print("The total order of operations is -", x)
print("The step by step order of operations is -", y)