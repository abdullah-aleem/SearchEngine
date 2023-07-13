import json 

with open('lexicon.json','r') as f:
    words = json.load(f)
with open('forwardIndex.json','r') as w:
    data=json.load(w)
invData=[]
for word in words:
    temp=[]

    for doc in data:
        title=list(doc.keys())[0]
        content=list(doc.values())[0]
        
        if word in content:
            temp.append(title)
    invData.append({word:temp}) 
    
with open("invertedIndex.json", "w+") as file:   
    json.dump(invData, file)