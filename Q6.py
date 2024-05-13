userInput = input("Enter score: ")
userInput = int(userInput)

if userInput in range(91, 101):
    print('A')
elif userInput in range(81, 91):
    print('B')
elif userInput in range(60, 81):
    print('C')
elif userInput in range(0, 60):
    print('D') 