# ques: take two comma separated inputs from user
#1. user's name 
#2. a single character

#output -2 print lines
#1. user's name length 
#2. count the character that user inputed 

#ans:
name , letter = input("enter your name and a letter: ").split(",")
print(f"length of your name is :{len(name)}")
print(f"character count : {name.strip().lower().count(letter.strip().lower())}")      #case sensitive
#Harshit - harshit
# H - h
# "Harshit"------->"Harshit"------>"harshit"
# "H" ------> "H" ------>"h"
name.strip().lower().count(letter.strip().lower())
letter.strip().lower()
