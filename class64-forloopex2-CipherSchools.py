# practice for loop 
# ask user a number a like 1256
# calculate sum of digits ---> 1+2+5+6

num =(input("enter a number: "))
total = 0
for i in range (0,len(num)):
    total += int(num[i])
print(total)
