#funtions and files

from sys import argv

script, file = argv

def print_file(file):
	print(file.read())
	
def rewind_file(file):
	file.seek(0)             #seek function finds the first character of a file if 0 is inside the argument. else it start from the argument listed in the function

def print_a_line(line, file):    
	print(line, file.readline()) # readline read the line where it last printed. if you mention the argument inside the readline, it prints it
	
current_file = open(file)
	
print("Let's print the file")
print_file(current_file)

print("Let's rewind")
rewind_file(current_file)
	
current_line = 1
print_a_line(current_line, current_file,)

current_line += 1
print_a_line(current_line, current_file)


