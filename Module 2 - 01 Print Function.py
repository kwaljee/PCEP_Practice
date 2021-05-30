# Module 2: print() function with sep and end

first_name = input("What is your first name?\n")
print("Hello,", first_name, "it's nice to meet you!", sep=" ", end="\n\n")

# string multiplication
print("    *" * 2)
print("   * *" * 2)
print("  *   *" * 2)
print(" *     *" * 2)
print("***   ***" * 2)
print("  *   *" * 2)
print("  *   *" * 2)
print("  *****" * 2)


# Data Types & Literals in Python

# string
a = "2"
print(type(a))

# integer
b = 2
print(type(b))

# float
c = 3.0
print(type(c))

# coding floats
c2 = 6.62607E-34
print(c2)
print(type(c2))

c3 = 0.00000001
print(c3)
print(type(c3))

# boolean
d = False
print(type(d))

# octal
e = 0o123
print(e)
print(type(e))

# hexidecmial
f = 0x123
print(f)
print(type(e))


#Scenario: Write a one-line piece of code, using the print() function, as well as the newline and escape characters, to match the expected result outputted on three lines.

# Expected output

# "I'm"
#""learning""
#"""Python"""

#Resulting Code
print("\"I'm\"\n", "learning\"\"\n", "\"Python\"\"\"", sep="\"")


