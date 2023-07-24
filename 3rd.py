counter=4
while True:
	password = input("Enter your passwaord ")
	print("...")
	if password == "lil":
		print("ACCES ALLOWED")
		break
	else: 
		print("ACCES DENIED")
		counter-=1
		print("You can only try  "+ str(counter))
		if counter==0:
			print("------")
			print("Your Locked Out")
			break
		
	
