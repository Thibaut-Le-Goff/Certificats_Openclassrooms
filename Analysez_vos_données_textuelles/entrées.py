from nltk.corpus import stopwords
import pandas as pd
import re

def entree_de_donnees(chemin_fichier_donnees):
    corpus_entraine = pd.read_csv(chemin_fichier_donnees)

    don_entraine = corpus_entraine["text"]

    if "target" in corpus_entraine.columns:
        pre_entraine = corpus_entraine["target"]

        return don_entraine, pre_entraine
    
    else :
        return don_entraine

def filtrage(don_entraine):
    """
    return re.sub(r'[^a-zA-Z0-9]', '', don_entraine)
    """

    liste_mots_stop = set(stopwords.words('english'))

    liste_de_mots = don_entraine.split()
    filtered_mots = [mot for mot in liste_de_mots 
                            if mot.lower() not in liste_mots_stop]
    
    return ' '.join(filtered_mots)
    
