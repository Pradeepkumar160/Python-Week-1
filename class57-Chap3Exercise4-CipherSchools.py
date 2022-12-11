#problem
#ask user input a number containing more than one  digit 
# example - 1256 , 1234
# calculate 1+2+5+6   and print

# algorithm (method to solve problem in human language)
# ask input in string i.e. dont change string to int
# example - "1256"
# pick string character one by one and change to int
# int(example[0] + int (example[1])..... go upto len(example)



#ans:
number = (input("enter a number: "))
#1256   #length =4  ,last index = 3
#int(number[i]) 

total =0
i = 0
while i < len(number):
    total +=int(number[i])
    i+=1
print(total)  
