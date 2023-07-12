import json
from cleaner import cleaning_text
import pandas as pd
import time
import os

# Path to the JSON file
file_path = "forwardIndex.json"



def forwardIndex(file):
    words=[]
    with open(file, "r") as file:
            # Load the JSON data
        
        data = json.load(file)
        if data:
            data=pd.Series(data)
            x=data.apply(cleaning_text,args=(words,))
            print(x[0])
    return x

app=forwardIndex("newsdata/cnbc.json")




# Check if the file exists
if os.path.exists(file_path):
    # File exists, open it and load the existing data
    with open(file_path, "r") as file:
        jdata = json.load(file)
else:
    # File doesn't exist, create an empty data dictionary
    jdata = []


# Save the updated data to the JSON file
jdata+=list(app)

with open(file_path, "w+") as file:
   
    json.dump(jdata, file)
