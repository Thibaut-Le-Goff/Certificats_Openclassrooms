
from entrées import *
import os
import nltk
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
 
chemin_dossier = os.path.dirname(os.path.abspath(__file__))
chemin_fichier_donnees = chemin_dossier + "\\nlp-getting-started\\train.csv"

# séparation des documents d'entrainementement de leur prédictions en deux groupes :
doc_entraine, pre_entraine = entree_de_donnees(chemin_fichier_donnees)

# filtrage des documents :
#nltk.download('stopwords')
doc_entraine_filtree = doc_entraine.apply(filtrage)

# séparation des documents lié à l'enentrainementement en deux groupes :
X_entraine, X_val, y_entraine, y_val = train_test_split(doc_entraine, pre_entraine, test_size=0.2, random_state=42)

# Vectorisation des documents :
modele_de_vectorisation = TfidfVectorizer(max_features=2500)
X_entraine_vecteur = modele_de_vectorisation.fit_transform(X_entraine)
X_val_vecteur = modele_de_vectorisation.transform(X_val)

# entrainement du modèle de prédiction :
modele_de_prediction = MultinomialNB()
modele_de_prediction.fit(X_entraine_vecteur, y_entraine)

# validation du model :
y_pred = modele_de_prediction.predict(X_val_vecteur)

precision = accuracy_score(y_val, y_pred)
print("Précision du modèle :", precision)
print(classification_report(y_val, y_pred))

#validation_data = pd.read_csv(path + "\\nlp-getting-started\\validation.csv")