import json
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.tokenize import RegexpTokenizer
import pandas
import time
#lexicons list
def lex(path):
    lexicons = []


   
    # regix to remove punctuations
    tokenizer = RegexpTokenizer(r'\w+')


    # create a porter object
    port = PorterStemmer()


    # load json file and conver to disctionary in python
    file = open(path, "r", encoding="utf8")
    data = json.load(file)
    print(len(data))
    
    # parsing on thecontents of data to remove stop words and dupicates
    data=pandas.DataFrame(data)

    # list of stop words in english
    stop_words = set(stopwords.words('english'))


    lexicons=data['content'].apply(lambda x: ' '.join(
    [port.stem(word) for word in x.split(" ") if word.lower() not in (stop_words)]))
    
    lexicons = lexicons.str.replace(r'[^\w\s]+','')


    lexicons = lexicons.str.split()

    l=[]
    
    lexicons=lexicons.values.tolist()
   
    for m in lexicons:
        l+=m
    # tem=[]
    # for m in data:
    #     temps=tokenizer.tokenize(m["content"])
    #     tem+=list(set([port.stem(w) for w in temps if not w.lower() in stop_words]))
    # lexicons=dict(enumerate(tem))  
    
   
    return (l)






