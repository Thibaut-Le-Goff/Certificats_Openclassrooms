import sqlite3

def creation_table(action, nom_table) :
    try:
        action.execute(
            f"CREATE TABLE {nom_table} ("
                "id INTEGER,"
                "name TEXT NOT NULL,"
                "jurisdiction TEXT,"
                "jurisdiction_description TEXT,"
                "incorporation_date DATE,"
                "status TEXT,"
                "service_provider TEXT,"
                "id_address INTEGER,"
                "source TEXT,"
                "note TEXT,"
                "end_date DATE,"
                "url TEXT,"
                "lifetime INTEGER,"
                "PRIMARY KEY(id)"
            ")"
        )
        resultat = action.fetchall()

        print("Résultat de la création de la table", nom_table, ":\n", resultat)

    except sqlite3.Error as erreur:
        print("La table n'a pas pu être créée :\n", erreur)

def suppression_table(action, nom_table) :
    try:
        action.execute(
            f"DROP TABLE {nom_table}"
        )
        resultat = action.fetchall()

        print("Résultat de la suppression de la table", nom_table, ":\n", resultat)
    
    except sqlite3.Error as erreur:
        print("La table n'a pas pu être supprimée :\n", erreur)

    """"""