import tkinter as tk
from tkinter import *
#from tkinter import ttk, Canvas
#from ttkthemes import ThemedTk, THEMES

window = Tk()
#tkinter themes
#window = ThemedTk(themebg=True)
#window.set_theme('breeze')
window.title("Main Window")
window.geometry('2100x2100')
window.configure(background='light blue')

def getvals():
    # add sample text to scrollbar to show the screen
    for i in range(1, 50):
        position = f'{i}.0'
        text.insert(position, f'Line {i}\n');

#creating rectangle
#w = Canvas(window, width=250, height=200)
#w.create_rectangle(0, 0, 100, 100, fill="blue", outline = 'blue')
#w.create_rectangle(50, 50, 100, 100, fill="red", outline = 'blue')
#w.pack()

#field names
se_name = Label(window, text='Search SYSTEM', font='ar 60 bold', padx=625, pady=100, bg='light blue', fg='blue')
se_name.grid(row=0, column=3)

#creating entry field
search_value = StringVar
searchEntry = Entry(window, textvariable=search_value, width=60, font=('Arial 16'))
searchEntry.grid(row=1, column=3, pady=20)

#to create scrollbar
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

#Creating search button
Button(text='Search', font='ar 12 bold', command=getvals).grid(row=3, column=3)

window.mainloop()
