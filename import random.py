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





import turtle as t 

def triangle() : 
    i = 1 
    while i < 4 : 
        t.forward(100)
        t.left(120)
        i = i + 1

triangle()


