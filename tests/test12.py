from tkinter import * 
from tkinter import ttk 


window = Tk() 
window.title("Title Name") 
window.config(bg='#FFFAFA')
window.geometry('1024x800')



rows = 0
while rows<50:
    window.rowconfigure(rows,weight=1)
    window.columnconfigure(rows, weight=1)
    rows +=1

#creation of frame
mainframe = ttk.Notebook(window,width=50)
mainframe.grid(row=1,column=2,columnspan=45,rowspan=43,sticky='NESW')

# create frame style
s = ttk.Style()
s.configure('new.TFrame', background='#7AC5CD')

#create tabs within the frame
tab1 = ttk.Frame(mainframe, style='new.TFrame')
mainframe.add(tab1, text="Tab1")


tab2 = ttk.Frame(mainframe, style='new.TFrame')
mainframe.add(tab2, text="Tab2")


tab3 = ttk.Frame(mainframe, style='new.TFrame')
mainframe.add(tab3, text="Tab3")

tab4 = ttk.Frame(mainframe, style='new.TFrame')
mainframe.add(tab4, text="Tab4")

tab5 = ttk.Frame(mainframe, style='new.TFrame')
mainframe.add(tab5, text="Tab4")

window.mainloop()