from  statistics import mean
from random import shuffle  

online_players = ["0","1","2","3"]
print (online_players [0])
print (online_players [len(online_players)-1])

online_players[0] = "Emre"

print (online_players)

online_players.insert(2, "Mehmet") 

print (online_players)

online_players[1:3] = ["onal","ryoko"]

print (online_players)

#rajouter un joueur a la fin 

online_players.append("JR")
online_players.extend(["jnr","ronaldo"])

print (online_players)

# un qui se déconnecte

del online_players[1]
online_players.pop(1)

print (online_players)

#supprimer un élément

online_players.remove("ronaldo")

print (online_players)

#remettre à zero

online_players.clear()

print (online_players)

#jouer a la maitresse 

notes = [ 8, 12, 10,
         9, 4, 20,
]

#module statistique

result = mean(notes)
shuffle(notes)
print(notes) 

print ("la moyenne de l'élève est de {}".format(result))