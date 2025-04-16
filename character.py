import random
import string
n=3
point=0
while n!=0:
 
    ch=random.choice(string.ascii_letters)
    print(ch)
    x= input("Enter the letter")
    if x==ch:
        point+=1
        print("Point is : ",point)
        
    else:
        n-=1
        print("wrong ")
        print(f"life is :{n}")

print(f"Total point is {point}")
    

