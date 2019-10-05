from spacy.tokenizer import Tokenizer
from spacy.lang.en import English

str = "Pythons live near the equator, in Asia and Africa, where it is hot and wet and their huge bodies can stay warm.  They make their homes in caves or in trees and have become used to living in cities and towns since people have been moving in on their territory."
nlp = English()

# Create a blank Tokenizer with just the English vocab
tokenizer = Tokenizer(nlp.vocab)
tokens = tokenizer(str)

for token in tokens:
    print(token)
