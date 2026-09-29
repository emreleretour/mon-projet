import random


n=random.randint(0,100  )
x= int(input("devinez la valeur"))
while x!= n:
    if x > n:
        print("c'est trop grand")
    else :
        print("c'est trop petit")
    x= int(input("devinez la valeur"))
print("gagné!")