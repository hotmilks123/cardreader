from tkinter import *

class Block:
    def __init__(self, master, func):
        self.ent = Entry(master, width=100)
        self.but = Button(master, 
                          text="Прочитать карту")
        self.but['command'] = eval('self.' + func)
        self.entryText = StringVar()
        self.entry = Entry(master, textvariable=self.entryText, width=100)
        self.ent.pack()
        self.but.pack()
        self.entry.pack()
    def getdata(self):
        res = "{0:d}".format(int(str(self.ent.get())[0:-2],16))
        self.entryText.set(str(res))
root = Tk()
block = Block(root, 'getdata')
root.mainloop()