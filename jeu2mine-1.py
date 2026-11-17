import random 


def creer(nL, nC, v=0):
    ligne = []
    for i in range(nC):
        ligne.append(v)

    bigL = []
    for i in range(nL):
        bigL.append(list(ligne))

    return bigL

def placeMine(p,m):
    nL=len(p)
    nc=len(p[0])
    for i in range(m):
        y=random.randint(0,nL-1)
        x=random.randint(0,nc-1)
        while p[y][x]==1:
            y=random.randint(0,nL-1)
            x=random.randint(0,nc-1)
        p[y][x]=1


p = creer(5,5)
print(p)
placeMine(p, 2)
print(p)