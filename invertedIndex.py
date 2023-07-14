import json 

with open('lexicon.json','r') as f:
    words = json.load(f)
with open('forwardIndex.json','r') as w:
    data=json.load(w)
invData={}
for word in words:
    temp=[]

    for title,content in data.items():

        if word in content:
            temp.append(title)
    invData[word]=temp 
    
with open("invertedIndex.json", "w+") as file:   
    json.dump(invData, file)