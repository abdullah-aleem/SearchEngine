import json
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.tokenize import RegexpTokenizer


# tokenizer = RegexpTokenizer(r'\w+')
# forwardInde = {}

# # create a porter object
# port = PorterStemmer()
# file = open('./tx.json', encoding="utf8")

# data = json.load(file)

# # parsing on thecontents of data to remove stop words and dupicates
# stop_words = set(stopwords.words('english'))

# forward index function

def forwardIndex(path):
    tokenizer = RegexpTokenizer(r'\w+')


    forwardInde = {}

    # create a porter object
    port = PorterStemmer()
    file = open(path, "r", encoding="utf8")

    data = json.load(file)

    # parsing on thecontents of data to remove stop words and dupicates
    stop_words = set(stopwords.words('english'))

# forward index function
    # global forwardInde
    tem = []
    
    for m in data:
        temps = tokenizer.tokenize(m["content"])
        
        # setting up forward index where docID is the id given
        forwardInde[m['id']] = [port.stem(w) for w in temps if not w.lower() in stop_words]
    return forwardInde
