import sqlite3

#
# Création de table entity
#

def creation_table_entity(action, nom_table) :
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
                "PRIMARY KEY(id),"
	            "FOREIGN KEY (id_address) REFERENCES address (id_address)"
            ")"
        )
        resultat = action.fetchall()

        print("Création de la table", nom_table, "réussie :\n", resultat)

    except sqlite3.Error as erreur:
        print("La table n'a pas pu être créée :\n", erreur)

#
# Création de table
#

def creation_table_compte(action, nom_table) :
    try:
        action.execute(
            f"CREATE TABLE {nom_table} ("
                "compte_mail TEXT,"
                "mail TEXT,"
                "nom TEXT,"
                "prenom TEXT,"
                "date_creation DATE,"
                "PRIMARY KEY (compte_mail, mail)"
            ")"
        )
        resultat = action.fetchall()

        print("Création de la table", nom_table, "réussie :\n", resultat)

    except sqlite3.Error as erreur:
        print("La table n'a pas pu être créée :\n", erreur)

#
# Suppression de table
#

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