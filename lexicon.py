import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import json

def cleaning_text(text):
    # Download the necessary data only once
    nltk.download('stopwords')
    nltk.download('punkt')

    # Get the set of English stop words
    stop_words = set(stopwords.words('english'))

    # Initialize the stemmer
    stemmer = PorterStemmer()

    # Tokenize the input text
    tokens = word_tokenize(text)

    # Remove the stop words and apply stemming
    processed_tokens = []
    for token in tokens:
        if token.lower() not in stop_words:
            stemmed_token = stemmer.stem(token)
            processed_tokens.append(stemmed_token)

    return processed_tokens


def lexicon(file):
    words=[]
    
    with open(file, 'r') as file:
        # Load the JSON data
        data = json.load(file)
        words+=cleaning_text(data[0]['content'])
    return words


print(lexicon("newsdata/whatreallyhappened.json"))
