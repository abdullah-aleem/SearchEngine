import json
import threading
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from lexicon import lex
from ForwardIIndex import forwardIndex
lexi = []
fI = {}
def start(path):

    
    invertedInde = {}



    # create a porter object
    port = PorterStemmer()
    file = open(path,"r", encoding="utf8")

    data = json.load(file)

    # parsing on thecontents of data to remove stop words and dupicates
    stop_words = set(stopwords.words('english'))
    
    # # lexicons and forwardIndex
    def l():
        global lexi
        lexi=lex(path)
      
    
    def f():
        global fI
        fI=forwardIndex(path)
        
        print("===================================================================================================================================================================")

    t1 = threading.Thread(target=l,args=())
    t2 = threading.Thread(target=f,args=())
    #starting the thread
    t1.start()
    t2.start()

    t1.join()
    t2.join()  
    f = open('invertedIndex.json', 'a')
    


    for i in lexi:
        invertedInde[i]=[]
        
        for k,v in fI.items():
            if i in v:
                invertedInde[i]+=[k]
   
    f.write(json.dumps(invertedInde))
    f.close()
   

# have thread to apply same function to two differrent files together
