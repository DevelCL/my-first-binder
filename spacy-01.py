# pip install spacy
# python -m spacy download es_core_news_sm

import spacy

# Load English tokenizer, tagger, parser, NER and word vectors
#nlp = spacy.load("en_core_web_sm")
nlp = spacy.load("es_core_news_sm")

# Process whole documents
text = ("Cuando Sebastian Thrun inició su trabajo en vehículos "
        "auto-conducidos en Google el 2007, pocas personas fuera "
        "de la compañía lo tomaron en serio. “Puedo decir que muchos "
        "altos ejecutivos de las principales compañías de vehículos "
        "norteamericanas me darían la mano y se alejarían porque "
        "no valía la pena hablar conmigo.” dijo Thrun, en una "
        "entrevista con Recode al inicio de esta semana.")
doc = nlp(text)

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)
