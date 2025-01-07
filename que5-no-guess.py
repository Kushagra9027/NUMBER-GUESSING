#--------------NO GUESSING-------------
import random
print("-------------------------------------")
print("--------NO GUESSING------------------")
print("YOU WILL HAVE 10 TRIES TO GUESS THE NO")
print("\n")
l=int(input("Enter the lowest no:"))
h=int(input("Enter the highest no:"))
a=random.randint(l,h)
tries=0
while tries<10:
    num=int(input("enter the number:"))
    tries=tries+1
    if num==a:
        print(f"CORRECT GUESS ,NO OF TRIES:{tries}")
        break
    elif num>a:
        print("High! Try again")
        print(f"NO of tries left:{10-tries}")
    elif num<a:
        print("Low! Try again")
        print(f"NO of tries left:{10-tries}")
print("\n")
print("-------------------------------------------")
        
    
    
        

    
    

