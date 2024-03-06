coins = 0
score = 0
wrong = 0

print("Welcome to the Roblox Quiz made by FanisPrograms on GitHub")
print("Let's get started!")
print("There are 3 questions")
print("Difficulty = Easy")

# Question 1
quest1 = input("Question #1 = When did Roblox get created? ")

# In Python, when you compare user input to a number, you should convert the user input to an integer using int(). For example, change lines like if quest1 == 2006: to if int(quest1) == 2006:

if int(quest1) == 2006:
    print("Correct!")
    score += 1
    shopquestion = input("Would you like to go to the shop? (Type 'y' to go to the shop and 'n' to continue): ")
    if shopquestion.lower() == "y":
        print("Welcome to the shop!")
        print("At this time we only have +1 score for 30 coins! Type 1 to buy the +1 score! ")

# You only need one = sign
        
        buy = input("What do you wanna buy? ")
        if int(buy) == 1:
            coins -= 30
            score += 1
            print("You have successfully bought +1 score for 30 coins")

else:
    print("Wrong")
    wrong += 1

# Question 2
quest2 = input("When did Arsenal release? ")
if int(quest2) == 2016:
    print("Correct!")
    score += 1
    shopquestion = input("Would you like to go to the shop? (Type 'y' to go to the shop and 'n' to continue): ")
    if shopquestion.lower() == "y":
        print("Welcome to the shop!")
        print("At this time we only have +1 score for 30 coins! Type 1 to buy the +1 score! ")
        buy = input("What do you wanna buy? ")
        if int(buy) == 1:
            coins -= 30
            score += 1
            print("You have successfully bought +1 score for 30 coins")

else:
    print("Wrong")
    wrong += 1

# Question 3
quest3 = input("When did Pet Sim X release? ")
if int(quest3) == 2021:
    print("Correct!")
    score += 1
    shopquestion = input("Would you like to go to the shop? (Type 'y' to go to the shop and 'n' to continue): ")
    if shopquestion.lower() == "y":
        print("Welcome to the shop!")
        print("At this time we only have +1 score for 30 coins! Type 1 to buy the +1 score! ")
        buy = input("What do you wanna buy? ")
        if int(buy) == 1:
            coins -= 30
            score += 1
            print("You have successfully bought +1 score for 30 coins")

else:
    print("Wrong")
    wrong += 1

# Question 4
quest4 = input("When did the Metaverse Champions event release? ")
if int(quest4) == 2021:
    print("Correct!")
    score += 1
    shopquestion = input("Would you like to go to the shop? (Type 'y' to go to the shop and 'n' to continue): ")
    if shopquestion.lower() == "y":
        print("Welcome to the shop!")
        print("At this time we only have +1 score for 30 coins! Type 1 to buy the +1 score! ")
        buy = input("What do you wanna buy? ")
        if int(buy) == 1:
            coins -= 30
            score += 1
            print("You have successfully bought +1 score for 30 coins")

else:
    print("Wrong")
    wrong += 1

print("Your score is", score)
print("Your wrong answers are", wrong)
