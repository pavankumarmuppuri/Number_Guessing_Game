#Join All Blocks to make our code works
import random
randNum = random.randint(1,100)
#print(randNum)

userName = input("Enter Your Name :")
print("Hello",userName," Welcome to Guessing Game")

#easyLevel = 10
#hardLevel = 5

guesses = (input("Choose 5 chances or 10 chances : "))
if guesses.isnumeric() == True :
  guesses = int(guesses)

if guesses == 5 :
  print("You have only 5 chances to guess the number")

  no_of_guesses = 0
  while no_of_guesses < 5 :
    userGuess = (input("Enter a number between 1 and 100 : "))
    if userGuess.isnumeric() == True :
      userGuess = int(userGuess)

      if userGuess > 100 or userGuess < 1:
        print("Please enter a number between 1 and 100 : ")
      if userGuess < 100 :
        if randNum == userGuess :
          print("Congrats your guess is correct")
          print("My number is : ",randNum)
          break

        elif randNum > userGuess :
          print("My number is greater than ",userGuess," , You have ",4-no_of_guesses," Chances left")

        else :
          print("My number is less than ",userGuess," , You have ",4-no_of_guesses," Chances left")
        no_of_guesses += 1

      if no_of_guesses >=5:
        print("Your chances are over")
        print("My number is : ",randNum)
    else :
      print("Please enter a number between 1 and 100 ")


elif guesses == 10 :
  print("You have 10 chances to guess the number")
  no_of_guesses = 0
  while no_of_guesses < 10 :
    userGuess = (input("Enter a number between 1 and 100 : "))
    if userGuess.isnumeric() == True :
      userGuess = int(userGuess)
      if userGuess > 100 :
        print("Please enter a number between 1 and 100")
      if userGuess < 100 :
        if randNum == userGuess :
          print("Conrgats your guess is correct")
          print("My number is : ",randNum)
          break


        elif randNum > userGuess :
          print("My number is greater than ",userGuess," , You have ",9-no_of_guesses," Chances left")

        else :
          print("My number is less than ",userGuess," , You have ",9-no_of_guesses," Chances left")
        no_of_guesses += 1

      if no_of_guesses >=10 :
        print("Your chances are over")
        print("My number is : ",randNum)
    else :
      print("Please enter a number between 1 and 100 ")

else :
  print("Please choose either 5 or 10 ")

#if guesses == 5 or 10 :
  #print("My number is : ",randNum)
