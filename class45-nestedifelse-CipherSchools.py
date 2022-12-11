#exercise :number guessing game and assign any number to it
# make a variable ,like winning_number and assgn any number to it.
# ask user to guess a number 
# if usewr guessed correctly then print "you win!!!"
# if user didn't guessed correctly then :
   #if user guessed lower than actual number then print "too low"
   # if user guessed higher than actual number then print "too high"

#bonus:
# google   "how to generate a random number in python " to generate random winning number 

#ans:
winning_number = 10
guessed_number = int(input("guess a number between 1 and 100: "))
if winning_number == guessed_number:
    print("you win!!!")
else:    
    if winning_number >guessed_number:
        print("too low")
    if winning_number <= guessed_number:
        print("too high")    
