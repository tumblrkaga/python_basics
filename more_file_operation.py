from sys import argv

script, filename =  argv

print("We are going to erase %r" % filename)
print("If you do noto want to erase press CTRL-C()")
print("If you do not want that, hit RETURN")
print("If you want to erase it, press ENTER")

input("?")

print("opening the file")
target = open(filename,'w')

print("truncating the file...")
target.truncate()
print("Now, I am going to ask you to print few lines")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I am going to write these to the file")

target. write(" %s \n %s \n %s" % (line1, line2, line3))
 
print("Finally, we have written the file and we close it")
target.close()


