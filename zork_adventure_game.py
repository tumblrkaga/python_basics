#Zork adventure game

def intro():
	print("You are in a room and there is door")
	print("You can: \n 1. Do the Macarena \n 2. Open the door \n 3. Commit Sucicide \n 4. Rage quit")
	
	choice = input(">>>")
	if choice == '1':
		print("You shake your belly")
	elif choice == '2':
		print("You open the door")
	elif choice =='3':
		print("Game over since you are dead!")
	elif choice =='4':
		print("Game Over")
	else:
		print("You have givern a wrong input. Please try again")
		intro()

intro()
