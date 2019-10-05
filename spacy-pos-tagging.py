import spacy

str = "Pythons live near the equator, in Asia and Africa, where it is hot and wet and their huge bodies can stay warm.  They make their homes in caves or in trees and have become used to living in cities and towns since people have been moving in on their territory."

nlp = spacy.load('en_core_web_sm')
doc = nlp(str)

doc[0]
# => Pythons

doc[0].pos
# => 91
