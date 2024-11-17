#perfect guess game

import random 
n = random.randint( 1,100)
a = -1 # yee isliye likha h kyuki agar loop mai kuch chal rha h to uska start batana jaruri hota h 
guess = 1 #same  as line no 3
#mai dono value ka start point kaha se h yee likhne k liye ye kiya h use 
while(a !=n): # iska matlab h ki jb tk yee condition true hogi tb tk yee run kre ga 
    a = int(input("Guess the number"))
    if(a>n):
        print("Lower number please")
        guess +=1
    elif(a<n):
        print("Higher number please")
        guess+=1   
print (f"you have gussa the number {n} correctly in {guess} gusses")
