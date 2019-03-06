from sys import argv

scripts, filename = argv # get the arguments in atore in teh variables

text = open(filename) #open the file that we have passed
print(text.read()) # after opening, reading the file and printing items

print("Type the file name again") 
file_again = input(">>>") #Try to get the file name again to print it again

text_again = open(file_again)#open the file and store it ina variable to read and print

print(text_again.read())# the values are printed when you read the content.