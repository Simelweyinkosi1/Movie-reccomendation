from pathlib import Path
import spacy
import os

# Load the spaCy model
nlp = spacy.load('en_core_web_md')

def watch_next(desc):
    data_folder = os.path.dirname(os.path.abspath(__file__))
    file_to_open = os.path.join(data_folder, "movies.txt")
    
    with open(file_to_open, "r") as movies_data:
        data = movies_data.read()

    movies = data.replace('\n', ' ').split(".")
    lst = {}
    for token in movies:
        token = nlp(token)
        result = token.similarity(desc)
        print()
        print(f"output {result:.2f} ")
        lst[token.text] = result

    max_value = max(lst, key=lst.get)
    return max_value

description = """Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator."""

print(watch_next(nlp(description)))
