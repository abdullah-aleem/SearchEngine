import json
from cleaner import cleaning_text
import pandas as pd


def lexicon(file):
    words = []
    
    with open(file, "r") as file:
        # Load the JSON data
        data = json.load(file)
    data=pd.Series(data)
    words=(data.apply(cleaning_text)).tolist()
        # for doc in data:
        #     words += cleaning_text(doc["content"].encode().decode())
        #     words += cleaning_text(doc["title"].encode().decode())
        #     print(words)
    return words


print(lexicon("newsdata/yahoonews.json"))
