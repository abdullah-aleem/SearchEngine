from tkinter import *
import tkinter as tk
import json
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.tokenize import RegexpTokenizer
import pandas
import time







#from tkinter import ttk, Canvas
#from ttkthemes import ThemedTk, THEMES

window = Tk()
# tkinter themes
#window = ThemedTk(themebg=True)
# window.set_theme('breeze')
window.title("Main Window")
window.geometry('2100x2100')
window.configure(background='thistle3')


def getvals():
    
    # add sample text to scrollbar to show the screen
    
    search = searchEntry.get()


    tokenizer = RegexpTokenizer(r'\w+')

    # create a porter object
    port = PorterStemmer()

    # load json file and conver to disctionary in python

    file = open("invertedIndex.json", "r", encoding="utf8")
    data = json.load(file)
    # # parsing on thecontents of data to remove stop words and dupicates
    # data=pandas.DataFrame(data)

    # list of stop words in english
    stop_words = set(stopwords.words('english'))
    words = tokenizer.tokenize(search)
    words = list(set([port.stem(w) for w in words if (not w.lower() in stop_words)
                    and (not (w.isdigit() or w[0] == '-' and w[1:].isdigit()))]))
    docs = []
    names = []
    for i in words:

        if not names == []:
            names = list(set(names) & set([v["doc"] for v in data.get(i, "")]))

        else:
            names = [v["doc"] for v in data.get(i, "")]

        docs += data.get(i, "")
    docs = sorted(docs, key=lambda x: x['hits'], reverse=True)
    x = []
    for i in docs:
        if i["doc"] in names and not i["doc"] in x:
            x += [i['doc']]

    for i in range(0, len(x)-1):
        position = f'{i}.0'
        text.insert(position, x[i]+"\n")


# field names
se_name = Label(window, text='Search SYSTEM', font='ar 60 bold',
                padx=625, pady=100, bg='thistle3', fg='thistle4')
se_name.grid(row=0, column=3)

# creating entry field
search_value = StringVar
searchEntry = Entry(window, 
                    width=60, font=('Arial 16'))
searchEntry.grid(row=1, column=3, pady=20)

# to create scrollbar
#window.resizable(False, False)

# apply the grid layout
window.grid_columnconfigure(0, weight=0)
window.grid_rowconfigure(0, weight=0)

# create the text widget
text = tk.Text(window, height=20)
text.grid(row=4, column=3, sticky=tk.EW)

# create a scrollbar widget and set its command to the text widget
scrollbar = Scrollbar(window, orient='vertical', command=text.yview, width=20)
scrollbar.grid(row=4, column=3, sticky=tk.NS)


#  communicate back to the scrollbar
text['yscrollcommand'] = scrollbar.set

# Creating search button
Button(text='Search', font='ar 12 bold', command=getvals).grid(row=3, column=3)

window.mainloop()