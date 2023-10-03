import sqlite3
from tables.visualisation import *
from tables.manipulation import *
from tables.insertion import *

def main():
    connection = sqlite3.connect('..\\..\\..\\..\\Downloads\\panamapapers\\panamapapers.sqlite3')
    action = connection.cursor()
    suppression_table(action, "entity2")

    # visualisation d'une table :
    nom_table = "entity1"
    nb_ligne = 10
    print("Les", nb_ligne, "premières lignes de la table", nom_table, "contienent :")
    voir_lignes(action, nb_ligne, nom_table)

    # création d'une table :
    nom_table = "entity2"
    creation_table_entity(action, nom_table)

    # insertion dans la table :
    donnees_a_ajouter = [
        (1, 'Une société', 'IMG', 'Le Pays Imaginaire', '2024-01-01', 'none', 'none', 0, 'none', 'none', '2026-01-01', 'none', 0),
        (2, 'Une autre société', 'IMG', 'Le Pays Imaginaire', '2025-01-01', 'none', 'none', 0, 'none', 'none', '2026-01-01', 'none', 0),
        (3, 'Encore une société', 'IMG', 'Le Pays Imaginaire', '2026-01-01', 'none', 'none', 0, 'none', 'none', '2026-01-01', 'none', 0)
    ]

    insertion_de_lignes(action, nom_table, donnees_a_ajouter)

    # visualisation de la table créée
    nb_ligne = 3
    print("Les", nb_ligne, "premières lignes de la table", nom_table, "contienent :")
    voir_lignes(action, nb_ligne, nom_table)

    # suppression d'une table :
    suppression_table(action, nom_table)

    nom_table = "compte2"
    creation_table_compte(action, nom_table)

    action.close()
    connection.close()

if __name__ == "__main__":
    main()