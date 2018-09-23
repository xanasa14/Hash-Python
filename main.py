# number to denote the number of elms in a tuple 
n = int(input())
# numbers to be hashed 
input_line = input()
#split them up to a list
input_list = input_line.split()
#We put the make them int from str to all elms in the list in this for loop 
for i in range(n):
    input_list[i] = int(input_list[i])
#Since we cant hash() a list, we gotta make them tuples     
t = tuple(input_list)
#We finally use the hash built-in function for the tuple we just created
print (hash(t))
