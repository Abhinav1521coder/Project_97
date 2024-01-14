import random

print("Number guessing game")
print("Guess a number between 1 and 15")
print("You get five chances to guess what the number is")

chance = 5
number= random.randint(1, 15)

while chance > 0:
    guess = int(input("Guess a number:"))
   
    if guess == number:
        print("You won!!")
        break
    elif (guess < number):
        print("Your guess was too low, guess higher than ", guess)
        chance -= 1 
    elif (guess > number):
        print("Your guess was too high, guess lower than ", guess)
        chance = chance - 1 
if(chance == 0):
    print("YOU LOSE the number is", number)