import json 

with open('lexicon.json','r') as f:
    words = json.load(f)
with open('forwardIndex.json','r') as w:
    data=json.load(w)
invData=[]
for word in words:
    temp=[]

    for doc in data:
        title=list(data[0].keys())[0]
        content=list(data[0].values())[0]
        if word in content:
            if title in temp:
                continue
            temp.append(title)
    invData.append({word:temp}) 