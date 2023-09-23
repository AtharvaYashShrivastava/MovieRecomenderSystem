# print('Atharva')
# name = input('What is your name ?')
# print('Hello ' + name)
# x = int(input("Enter your Birth Date"))
# print(x)


# There are 3 types of Data types:

    #Fundamental data types 
#     The fundamental data type includes 
# list 
# bool
# tuple
# set 
# dict
# int
# float


    # class data types -> Custom data types



    # specialized data types -> These includes importing modules from libraries
print(2+4)
print(type(2+4))
print(round(2.3))   # round keyword helps us to round off the vlues 
print(abs(-45))     # abs keyword helps u to find the absolute value of a number
print(bin(5))       # helps you to print binary number of a digit 
print(complex(3))   # helps you to pint complex numbers of a number : The representation 
print(int('0b101',2 )) # This represnts that the given binary number has been succesfully convert into an integer numbet 


print(type('hello'))  # this is a string class
long_string = ''' 
Wow Amazing                         # thed long string is enclosed within 3 single quotes 
0 0
---
'''
print(long_string)

print(str(100))
print(type(str(100)))

# FORMATTED STRINGS

name = 'Atharva'
age = 20

print(f'Hi {name} you are {age} yeas old') # Adding f before the staert of the sting and adding{ } helps you to remove the making reference 


# Indexing Of Strings

selfos = 'Hello'
print(selfos[0:6])

# Stings are immutable and can not be replaced the origional sting however,

str1 = ' hey this is me '
str2 = str1.replace('i', 'u')
print(str2)

# Excersise
 # You need to convert the data type as it is by default set to string and we need o convert it into a integer
current = int(input('What year were you born ?'))
currentage = 2023-current
print(f'your age is {currentage}')