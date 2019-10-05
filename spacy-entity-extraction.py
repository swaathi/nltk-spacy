import spacy

str = "Pythons live near the equator, in Asia and Africa, where it is hot and wet and their huge bodies can stay warm.  They make their homes in caves or in trees and have become used to living in cities and towns since people have been moving in on their territory."

doc = nlp(str)

entities = [(i, i.label_) for i in doc.ents]
entities

# Out[10]: [(Asia, 'LOC'), (Africa, 'LOC')]
