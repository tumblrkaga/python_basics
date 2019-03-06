#function can return something

def add(a, b):
	return(a + b)

def subtract(a, b):
	return(a - b) 
	
def multiply(a, b):
	return(a * b)

def divide(a, b):
	return(a / b)

age = add(3, 70)
height = subtract(87, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print(what)

whatt = multiply(divide(height, weight), subtract(height, iq))
print(whatt)