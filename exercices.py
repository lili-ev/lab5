
classe = [
    ["Alice", 20, 15],
    ["Bob", 19, 12],
    ["Charlie", 21, 18],
    ["Diana", 20, 14]
]

print("Classe initiale :")
print(classe)

# Tri par note décroissante
classe.sort(key=lambda ligne: ligne[2], reverse=True)
print("\n1) Classe triée par note décroissante :")
print(classe)

# Calcul de la moyenne des notes
somme_notes = 0
for etudiant in classe:
    somme_notes += etudiant[2]

moyenne = somme_notes / len(classe)

print("\n1) Moyenne des notes :", moyenne)


# Demander un nom à l'utilisateur (tu peux modifier si tu veux)
recherche_nom = input("\n2) Entrer un nom à rechercher : ")

# Chercher dans la classe
resultat = None
for nom, age, note in classe:
    if nom.lower() == recherche_nom.lower():
        resultat = [nom, age, note]
        break

if resultat:
    print("Étudiant trouvé :", resultat)
else:
    print("Aucun étudiant trouvé avec ce nom.")

# BONUS : version avec next()
print("\n2) Bonus : utilisation de next()")

resultat2 = next(
    (etudiant for etudiant in classe if etudiant[0].lower() == recherche_nom.lower()),
    None
)

print("Résultat avec next() :", resultat2)


# Copie superficielle : [:]
classe_copie = classe[:]

# On modifie dans la copie
classe_copie[0][1] = 99  

print("\n3) Après modification dans classe_copie :")
print("classe_copie :", classe_copie)
print("classe (originale) :", classe)
print("→ On voit que l'original change aussi ! (copie superficielle)")


# Copie profonde avec deepcopy
import copy
classe_profonde = copy.deepcopy(classe)

classe_profonde[0][1] = 50

print("\n3) Après modification dans copie profonde :")
print("classe_profonde :", classe_profonde)
print("classe (originale) :", classe)
print("→ L'original NE change PAS (copie profonde)")


# Transformer en liste de dictionnaires
classe_dict = [
    {"nom": etu[0], "age": etu[1], "note": etu[2]}
    for etu in classe
]

print("\n4) Classe convertie en dictionnaires :")
print(classe_dict)

# Exemple d'accès par clé :
print("\nExemple : accès au nom du premier étudiant :", classe_dict[0]["nom"])
