score = 0
wrong = 0
print ("Welcome to the Roblox Quiz made by FanisPrograms on GitHub")
print ("Let's get started!")
print ("There are 3 questions")
print ("Difficulty = Easy")
quest1 = input ("Question #1 = When did Roblox get created? ")
if quest1 == 2006 :
    print ("Correct!")
    score += 1
else:
    print ("Wrong")
    wrong += 1

quest2 = input ("When did Arsenal release? ")
if quest1 == 2016 :
    print ("Correct!")
    score += 1
else:
    print ("Wrong")
    wrong += 1

quest3 = input ("When did Pet Sim X release? ")
if quest1 == 2021 :
    print ("Correct!")
    score += 1
else:
    print ("Wrong")
    wrong += 1

print ("Your score is", score)
print ("Your wrong answers are", wrong)


