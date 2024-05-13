dayList = {"1": "Sunday",
           "2": "Monday",
           "3": "Tuesday",
           "4": "Wednesday",
           "5": "Thursday",
           "6": "Friday",
           "7": "Saturday"}

userInput = input("Enter number between 1 and 7: ")
if int(userInput) in range(1, 8):
    print(dayList[userInput])
