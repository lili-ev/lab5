classe = [
    ["Alice", 20, 15],
    ["Bob", 19, 12],
    ["Charlie", 21, 18],
    ["Diana", 20, 14]
]

print("Classe initiale :")
print(classe)
liste1 = [1, 2, 3]
liste2 = [4, 5]
liste_bonne = [1, 2, 3]
liste_bonne.extend(liste2)
print(liste_bonne) 

notes = [note for _, _, note in classe if note >= 15]
print("Notes >= 15 :", notes)

from pprint import pprint
pprint(classe) 
