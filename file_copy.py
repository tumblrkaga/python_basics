#Copy files from one file to the other

from sys import argv

script, input, output = argv

print("Copy the files from file1 to file2")

in_file = open(input)
in_data = in_file.read()

print("the input file is %d bytes long" %len(in_data))
print("Ready to print the file ..press CTRL + C to abort")


out_file = open(output, 'w')
out_file.write(in_data)

print("All right, all done")

out_file.close()
in_file.close()