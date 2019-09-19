# creating varibale

my_variable=10

#increasing the variable

my_variable=my_variable + 3

print(my_variable)

#store a literal string 

my_variable="yellow"

print(my_variable)

#string with ""

string1="hey there"
string2="i am here"

print(string1 + " " + string2)

#place backslash before a double quote if string is encloded in double quotes
txt="He said: \"You should get the same results no matter how you choose to enclose a string.\""
print(txt)


#string with ''
string3='good morning'

print(string3)

#accessing the first character on the string

s="prerna"
print(s[0])

#accessing the last character on the string

print(s[len(s)-1])

print(s[-1])

print(s[-2])

#concatenating string

print("Hello"+"python")

#repeating the string

s="*****"
print(s*5)

#length of the string

len("world")

#slicing string

var="Programe"
print(var[3:5])

print(var[3:6])
print(var[4:])

print(var.lower())

print(var.upper())

#str()

pi=3.1416
str(pi)
print("this is my fvrt number"+str(pi))

#octal literal
p=0o7
print(p)

#hexa desimal literals

hex_lit=0xA0C
print(hex_lit)

#binary literal

c=0b1100
print(c)

#convert the integer to octal literal

print(oct(7))

#convert the integer to hexadesimal

print(hex(2572))

#convert the integer to binary string

print(bin(12))

#defining the variable with thehex()

x=hex(2572)
print(x)

type(x)

print(6.2e3)

#complex number

a=2+5j
b=4-2j
c=a+b
print(c)

print(float(12))

print(int(12))

print(complex(12)(12+0j))
