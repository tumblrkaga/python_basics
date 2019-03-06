#% is the format string that is available in python.
#Let us do an exercise to find how to use it

my_name = 'Shaf'
my_age = 25
my_height = 78
my_eyes = 'Blue'
print("My name is %s " % my_name)#remember  to use %s for string
print("My age is %d" % my_age)#remember  to use %d for numeric
print("If I add %d and %d I get %d" % ( my_age, my_height,  my_age + my_height))
print("My name is %r, %r" % (my_name, my_age)) # print my name and my age which are of different datatypes. %r prints no motter what the data type is

 # Other format characters in python
# d	Signed integer decimal.	
# i	Signed integer decimal.	
# o	Unsigned octal.	(1)
# u	Unsigned decimal.	
# x	Unsigned hexadecimal (lowercase).	(2)
# X	Unsigned hexadecimal (uppercase).	(2)
# e	Floating point exponential format (lowercase).	
# E	Floating point exponential format (uppercase).	
# f	Floating point decimal format.	
# F	Floating point decimal format.	
# g	Same as "e" if exponent is greater than -4 or less than precision, "f" otherwise.	
# G	Same as "E" if exponent is greater than -4 or less than precision, "F" otherwise.	
# c	Single character (accepts integer or single character string).	
# r	String (converts any python object using repr()).	(3)
# s	String (converts any python object using str()).	(4)
# %	No argument is converted, results in a "%" character in the result.	