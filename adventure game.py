import random
name = str(input("Enter your Name =  \n"))
print(f"{name} You are stuck in a forest. Your task is to get out from the forest without dieing")
print("You are walking threw forest and suddenly a wolf comes in your way. Now you have two options.")
print("1. Run \n2. Climb the nearest Tree")
user = int(input("Choose one option 1 or 2 ? \n"))
if user==1:
    print("You Died !!")
elif user==2:
    print("hurray!!,You Survived!!")
else:
    print("Incorrect Input")