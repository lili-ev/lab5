#Instancie une liste initiale:
etudiants = ["Alice", "Bob", "Charlie"]
print(etudiants) 

#Ajoute un élément à la fin avec append() :
etudiants.append("Diana")
print(etudiants)

#Insère à une position précise avec insert() :
etudiants.insert(1, "Eve")  
print(etudiants)

#Supprime par valeur avec remove() (enlève la première occurrence) :
etudiants.remove("Bob")
print(etudiants)
  
#Retire et récupère le dernier élément avec pop() :
dernier = etudiants.pop()
print(dernier)   
print(etudiants)   

#Index positif :
print(etudiants[0])  
print(etudiants[2])  
#Index négatif :
print(etudiants[-1]) 
print(etudiants[-2])  