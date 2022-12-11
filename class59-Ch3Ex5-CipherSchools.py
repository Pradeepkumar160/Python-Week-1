# ask user for name 
# example - "Pradeep"
#print count of each words
# output:
        #   p : 2
        #   r : 1
        #   a : 1
        #   d : 1
        #   e : 2
        #   e : 2
        #   p : 2


# ans :
name =input("enter your name : ")
# Pradeep
# name.count("p") , name.count(name[0]) = 2
# name.count("r") , name.count(name[1]) = 1
# name.count("a") , name.count(name[2]) = 1
# name.count("d") , name.count(name[3]) = 1
# name.count("e") , name.count(name[4]) = 2
# name.count("e") , name.count(name[5]) = 2
# name.count("p") , name.count(name[5]) = 2

#output

i = 0
temp_var = ""
while i< len(name):
    if name[i] not in temp_var:
        temp_var +=name[i] 
        print(f"{name[i]} : {name.count(name[i])}")
        i+=1
