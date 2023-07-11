import json
from cleaner import cleaning_text
import pandas as pd
import time



def forwardIndex(file):
    words=[]
    with open(file, "r") as file:
            # Load the JSON data
        
        data = json.load(file)
        if data:
            data=pd.Series(data)
            x=data.apply(cleaning_text,args=(words,))
            print(x[0])
    return words

forwardIndex("newsdata/newsbud.json")