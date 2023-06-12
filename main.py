import multiprocessing
from ForwardIIndex import forwardIndex
from lexicon import lex
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import json

import threading
import os
import glob
import pprint
import time





lexi = []
fI = {}


def start(path):
    now=path
    path = './test/'+path
    invertedInde = {}

    # create a porter object
    port = PorterStemmer()
    file = open(path, "r", encoding="utf8")

    data = json.load(file)

    # parsing on thecontents of data to remove stop words and dupicates
    stop_words = set(stopwords.words('english'))

    # # lexicons and forwardIndex
    def l():
        global lexi
        lexi = lex(path)

    def fw():
        global fI
        fI = forwardIndex(path)

        print("===================================================================================================================================================================")

    t1 = threading.Thread(target=l, args=())
    t2 = threading.Thread(target=fw, args=())
    # starting the thread
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    # lexi=lex(path);
    # fI=forwardIndex(path)
    name = "invertedIndex"
    f = open(name, 'a')

    print(len(lexi))
    for i in lexi:
        invertedInde[i] = []

        for k, v in fI.items():
            if i in v:
                invertedInde[i] += [{"doc":k,"hits":v.count(i)}]

    f.write(json.dumps(invertedInde))
    f.close()




if __name__ == '__main__':
    # Get the list of filenames in the directory
    filenames = os.listdir('./test/')

    # Create a pool of workers
    with multiprocessing.Pool(processes=4) as pool:
        # Map the process_file function to the list of filenames
        pool.map(start, filenames)




