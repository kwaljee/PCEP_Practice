# Operators


# Asterisk
print(2*3) # multiplication
print(2**3) # exponential multiplication

# Slash
print()
print(6/2, " One slash division with float output")
print(6/4, " One slash division with float output in decimals no rounding")
print(6//2, "   Two slash division with no float output rounded values")
print(6//5, "   Two slash division with no float output rounded values")
print(6.0//4, " Two slash rounded with decimals because numerator value in decmial format")
print(11//4.0, " Two slash rounded with decimals because denominator value provides float")
print(4.3//2, "neareset decimal")


# Percent symbol (modulo operator)
print()
print (6%3, "modulo operator remainder whereby output is 0")
print (6%4, "modulo operator remainder whereby output is 2")
print(12 % 4.5)

#Right sided binding example
print()
print(2 ** 2 ** 3)

# Examples
print()
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2) # output is 10.0
print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4)) # -0.5 0.5 0 -1
print((2 % -4), (2 % 4), (2 ** 3 ** 2)) # -2 2 512
