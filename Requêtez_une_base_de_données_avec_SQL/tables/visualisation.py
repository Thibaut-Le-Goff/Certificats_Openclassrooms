import sqlite3

def voir_lignes(action, nb_lignes, nom_table):
    try:
        action.execute(f"SELECT * FROM {nom_table}")

        result = action.fetchall()

        nb_lignes = 0
        for row in result :
            print(row)
            nb_lignes = nb_lignes + 1

            if nb_lignes == 10 :
                break

    except sqlite3.Error as erreur:
        print("La table n'a pas pu être visualisée :\n", erreur)