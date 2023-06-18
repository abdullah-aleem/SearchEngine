
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Precompile regular expression pattern
punctuation_pattern = re.compile(r"[^a-zA-Z\s]")

# Create stop words set
stop_words = set(stopwords.words("english"))

# Initialize the stemmer
stemmer = PorterStemmer()

def cleaning_text(text):
    # Tokenize the input text
    text=text['content'].encode().decode()
    tokens = word_tokenize(text)

    # Remove the stop words and apply stemming using list comprehension
    processed_tokens = [
        stemmer.stem(punctuation_pattern.sub("", token))
        for token in tokens
        if (token.lower() not in stop_words) and punctuation_pattern.sub("", token).strip()
    ]
    return processed_tokens 