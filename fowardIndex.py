import json
from cleaner import cleaning_text
import pandas as pd
import time
import os
import multiprocessing
# Path to the JSON file
file_path = "forwardIndex.json"
directory="newsdata/"
app=[]

def forwardIndex(file):
    global app
    print("hello this is forward index")
    words=[]
    with open(file, "r") as file:
            # Load the JSON data
        
        data = json.load(file)
        if data:
            data=pd.Series(data)
            x=data.apply(cleaning_text,args=(words,))
            x=list(x)
            app+=x
    return x

# app=forwardIndex("newsdata/cnbc.json")
if __name__=='__main__':
    
    # Get the list of files in the directory
    file_list = os.listdir(directory)

    # Create a multiprocessing Pool with the number of desired processes
    pool = multiprocessing.Pool()

    # Map the process_file function to each file in the file_list
    # This will start a new process for each file
    pool.map(forwardIndex, [os.path.join(directory, file) for file in file_list])

    # Close the pool to prevent any more processes from being started
    pool.close()

    # Wait for all the processes to finish
    pool.join()


    # Check if the file exists
    if os.path.exists(file_path):
        # File exists, open it and load the existing data
        with open(file_path, "r") as file:
            jdata = json.load(file)
    else:
        # File doesn't exist, create an empty data dictionary
        jdata = {}
    # Save the updated data to the JSON file



    for y in list(app):
        
        jdata.update(y)
    with open(file_path, "w+") as file:
        json.dump(jdata, file)
