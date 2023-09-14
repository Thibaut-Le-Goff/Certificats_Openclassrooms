from nltk import RegexpTokenizer

def tokenize_document(document):
    tokenizer = RegexpTokenizer(r'\w+')
    list_mots = tokenizer.tokenize(document)

    return list_mots

document = "Bonjour, je suis un document d'exemple pour le cours d'Openclassrooms. Soyez attentifs à ce cours !"
list_mots = tokenize_document(document)
print(list_mots)
