formatter = '%r %r %r %r'

print(formatter % (1,2,3,4)) 
print(formatter % ('a', 'b', 'c', 'd'))
print(formatter % (True, False, True, False))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % ( 'I had it' , 't"s enough for me', 'please proceed', 'bye ! See you.'))
# As you seen in the previous exercises, if you are thinking to enclose a apostrophe(') or double quotes(") in your sentence, we have to enclose the sentence in 
# double quotes if you need single quote and vice versa.

#Note: %r is used for debugging to know the raw value of the variable used by the programmer 