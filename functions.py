#prgram with funtions

def print_args(*args):
	one, two = args
	print(one, two)

def print_one(arg):
	one = arg
	print(one)

def print_two(arg1, arg2):
	print(arg1, arg2)
	
def no_arg():
	print("I have noting to print")

print_args(1,2)
print_one("I am the only value")
print_two("I am 1st variable value", "I am second variable value")
no_arg()