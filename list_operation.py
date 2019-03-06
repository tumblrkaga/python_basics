#List operation
count = [1, 2, 3, 4, 5, 6, 7]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']


for number in count:
	print("The numbers in the list are %d" %number)

for fruit in fruits:
	print("I have %r fruits in my basket" %fruit)
	
elements = []

for i in range(0, 6):
	print("adding %d to the list" %i)
	elements.append(i) #add elements to the list

print(elements)	
#acessing the elemnets in the list
print(fruits[0])#access the first element
print(fruits[-1])#prints the last element
print(change[2:4])#prints the elements in the second and 3rd index which is splicing
print(change[:-1])
print(count.count(1)) #how many 1s are in the list count

fruits.extend(['apple','grape', 'plum'])

print(fruits)

del fruits[4]

print(fruits)