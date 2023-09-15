print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay let's play :)")
score = 0

answer = input("What does a CPU stands for? ")
if answer.lower() == "central processing unit":
    print("correct")
    score += 1
else:
    print("incorrect!")

answer = input("What does a GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print("correct")
    score += 1
else:
    print("incorrect")

answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print("correct")
    score += 1
else:
    print("incorrect")

answer = input("What does PSU stands for? ")
if answer.lower() == "power supply unit":
    print("correct")
    score += 1
else:
    print("incorrect!")

print("Your score is "+str(score))
print("your percentage is " +str((score/4)*100)+"%")