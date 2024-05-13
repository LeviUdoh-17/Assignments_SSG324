birthday = {"Levi": "June 4",
            "Bimbo": "June 19",
            "Israel": "October 6",
            "Perez": "June 10",
            "Rita": "April 10",
            "Tinuke": "November 11"}
print("Levi")
userInput = input("Enter a name: ")
names = birthday.keys()
if userInput in names:
    print(birthday[userInput] + " is the birthday of " + userInput)
else:
    print(f"I do not have birthday information for {userInput}")