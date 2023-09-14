import sqlite3

def insertion_de_lignes(action, nom_table, donnees_a_ajouter):
    try:
        places_reservees = ', '.join(['?' for _ in range(len(donnees_a_ajouter[0]))])

        requete = f"INSERT INTO {nom_table} VALUES ({places_reservees})"

        action.executemany(requete, donnees_a_ajouter)

    except sqlite3.Error as erreur:
        print("Les données n'ont pas pu être ajoutées : \n", erreur)
        