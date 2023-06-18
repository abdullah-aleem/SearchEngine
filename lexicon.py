import json
from cleaner import cleaning_text
import pandas as pd
import time




def lexicon(file):
    words = []
    
    with open(file, "r") as file:
        # Load the JSON data
    
        data = json.load(file)
    if data:
  
        data=pd.Series(data)
        data.apply(cleaning_text,args=(words,))
    return words


start_time = time.time()  # Start measuring time
result = lexicon("newsdata/yahoonews.json")
end_time = time.time()  # Stop measuring time
execution_time = end_time - start_time

# print("Lexicon:", result)
print("Execution Time:", execution_time, "seconds")