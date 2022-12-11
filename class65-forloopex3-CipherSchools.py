# ask user for name 
# example - "Pradeep"
#print count of each words
# output:
        #   P : 2
        #   R : 1
        #   A : 1
        #   D : 1
        #   E : 2
        #   E : 2
        #   P : 2


#ans:
name = input("enter a name : ")
temp = "" 
for i in range (0,len(name)):
    if name[i] not in temp:
        print(f"{name[i]}: {name.count(name[i])}")
        temp += name[i]
