from emoji import emojize
import emoji

def menu():
	print("[1] dog 1")
	print("[2] cat 2")
	print("[0] Exit the program.")

menu()
option = int(input("Select your spirit animal: "))

while option != 0:
	if option == 1:
		# do option 1
		print(emojize(":dog_face:"))
	elif option == 2:
		# do option 2
		print(emojize(":grinning_cat:"))
	else:
		print("Invalid option.")

	print()
	menu()
	option = int(input("Enter your option: "))

print("Keep updating our spirit animals list")