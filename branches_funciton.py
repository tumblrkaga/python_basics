from sys import exit

def gold_room():
	print("This room is full of gold. How much do you take?")
	next  =  input(">")
	
	if "0" in next or "1" in next:
		how_much = int(next)
	else:
		dead("Man, learn to type a number")
		
	if how_much < 50:
		print("Nice, you're not greedy")
		exit(0)
	else:
		dead("You are greedy bastard")
	

def bear_room():
	print("There is a bear in this room")
	print("the bear has bunch of honey")
	print("the fat bear is in front of another door")
	print("How are you going to move the bear?")
	bear_moved = False
	
	while True:
		next =  input(">")
		
		if next == "take honey":
			dead("The bear looks at you then slaps your face off")
		elif next == "taunt bear" and not(bear_moved):
			print("The bear gets pissed off andchews your leg off")
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off")
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print("I got no idea what that means")

def cthulhu_room():
	print("here you see the great evil Cthulu")
	print("He, it, whatever stares at you and you go insane")
	print("Do you flee for your life or eat your head?")
	
	next = input(">")
	
	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	else:
		cthulhu_room()

def dead(why):
	print(why, "Good job!")
	exit(0)

def start():
	print("you are in a dark room")
	print("There is a door to your right and left")
	print("Which one do you take?")
	
	next = input(">")
	
	if next == "left":
		bear_room()
	if next == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve")

start()
