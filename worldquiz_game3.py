print("Welcome to World quiz!")
playing = input("Do you want to proceed? ")

if playing.lower() != "yes" :
    quit()

print("Okay! Let's begin the fun :)")
score = 0

answer = input("Which is the largest animal in the world? ")
if answer.lower() == "blue whale":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
answer = input("Which is the most widely spoken language in the world? ")
if answer.lower() == "mandarin":
    print('Correct!')
    score +=1
else:
    print('Incorrect!')
answer = input("Which language is used by the computer to process data? ")
if answer.lower() == "binary":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
answer = input("Which is the most sensitive organ in our body? ")
if answer.lower() == "skin":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
answer = input("Which planet is known as Red planet? ")
if answer.lower() == "mars":
    print('Correct!')
    score += 1
else:
    print('Incorrect')
answer = input("What makes up 80% of our brain? ")
if answer.lower() == "water":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
answer = input("How many cricket world cups does India have? ")
if answer.lower() == "two":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
answer = input("Which is the hottest continent on earth? ")
if answer.lower() == "africa":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
answer = input("Which is the longest river on the earth? ")
if answer.lower() == "nile":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
answer = input("Which month of the year has least number of days in it? ")
if answer.lower() == "february":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
print("You got " + str(score) + "questions correct!")
print("You got "+ str((score/10) * 100) + "%")