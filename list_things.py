ten_things =  "apples Oranges crows Telephone Light sugar"
print(" wait there's not 10 things n that list, let's fix that.")

stuff = ten_things.split(' ')
more_stuff =  ["day", "night", "song", "corn", "banana"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print("appending %r" %next_one)
	stuff.append(next_one)

print("there we go", stuff)
print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff))
print('#'.join(stuff[3:5]))