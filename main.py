from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import re
import json
# Precompile regular expression pattern
punctuation_pattern = re.compile(r"[^a-zA-Z\s]")

# Create stop words set
stop_words = set(stopwords.words("english"))

# Initialize the stemmer
stemmer = PorterStemmer()


##to have only articles where all words exist
def common(lit):
    sets=[set(lst) for lst in lit]
    
    return set.intersection(*sets)



print("Enter what you want to search ")
search=input()
tex=search.encode().decode()
tokens = word_tokenize(tex)
processed_tokens = [
        stemmer.stem(punctuation_pattern.sub("", token))
        for token in tokens
        if (token.lower() not in stop_words) and punctuation_pattern.sub("", token).strip()
    ]
with open("invertedIndex.json",'r') as f:
    data=json.load(f)
answer=[]
for t in processed_tokens:
    answer+=[data.get(t,[])]
answer=common(answer)
for x in answer:
    print(x)
