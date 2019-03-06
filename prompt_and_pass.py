from sys import argv

script, username = argv
prompt = '>'

print("I am %r. I would like to ask you few questions %r'" %( script, username))
print("Do you like me?")
likes = input(prompt)

print("Where do you live?")
lives = input(prompt)

print("Well, you said %r  about liking me" % likes)
print("You live in %s" %lives)
print("Thanks for your info")

