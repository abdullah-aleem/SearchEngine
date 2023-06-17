import json
from cleaner import cleaning_text



def lexicon(file):
    words = []

    with open(file, "r") as file:
        # Load the JSON data
        data = json.load(file)
        for doc in data:
            words += cleaning_text(doc["content"].encode().decode())
            words += cleaning_text(doc["title"].encode().decode())
            print(words)
    return words


print(lexicon("newsdata/whatreallyhappened.json"))
