#functions and variables

def apples_and_oranges(apple_count, orange_count):
	print("You have %d apples and %d oranges" %(apple_count, orange_count))

print("The number of apples and oranges canbe gven via passing arguments")
apples_and_oranges(10,12)

print("We can use variable from our script as well")
apple_count = 20
orange_count = 25

apples_and_oranges(apple_count,orange_count)

print("We can even do math inside too")
apples_and_oranges(10+3, 6+7)

print("Also, add values to the variables")

apples_and_oranges(apple_count + 5, orange_count + 8)