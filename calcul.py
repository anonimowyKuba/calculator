from tkinter import *
from math import sqrt

#fatorial function - not use! yet..
def fact(n):
    if n>1:
        return n*fact(n-1)
    else:
        return(1)
    

class Obliczacz:
    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator")

        self.screen=Text(master,state="disabled", width=50,height=4,background="green2")
        self.screen.grid(row=0,column=0,columnspan=5,padx=10,pady=10)
        self.screen.configure(state="normal")
        self.equation=""

        b1 = self.createButton(7)
        b2 = self.createButton(8)
        b3 = self.createButton(9)
        b33= self.createButton('(')
        b4 = self.createButton('CE',None)
        
        b5 = self.createButton(4)
        b6 = self.createButton(5)
        b7 = self.createButton(6)
        b77= self.createButton(')')
        b8 = self.createButton('/')
        
        b9 = self.createButton(1)
        b10 = self.createButton(2)
        b11 = self.createButton(3)
        b12 = self.createButton('*')
        b122= self.createButton("\u02c4")
        
        b13 = self.createButton('.')
        b14 = self.createButton(0)
        b15 = self.createButton('+')
        b16 = self.createButton('-')
        b166= self.createButton('\u221A')
        
        b17 = self.createButton('=',None,34)

        buttons = [b1,b2,b3,b33,b4,b5,b6,b7,b77,b8,b9,b10,b11,b12,b122,b13,b14,b15,b16,b166,b17]

        licz=0
        for row1 in range(1,5):
            for col in range(5):
                buttons[licz].grid(row=row1,column=col)
                licz+=1
        buttons[20].grid(row=6,column=0,columnspan=5)

    def createButton(self,val,write=True,width=10):
        return Button(self.master,text=val,command = lambda:
                      self.click(val,write),width=width)

    def click(self,text,write):
        if write==None:
            if text=="=" and self.equation:
                self.equation= re.sub("\u02c4", '**', self.equation)
                ans=str(eval(self.equation))
                print(self.equation, "=", ans)
                self.clear_screen()
                self.insert_screen(ans,newline=True)
            elif text =="CE":
                self.clear_screen()
        elif text=='\u221A':
            ans=str(sqrt(int(eval(self.equation))))
            print("sqrt(",self.equation,') =',ans)
            self.clear_screen()
            self.insert_screen(ans,newline=True)
        else:
            self.insert_screen(text)
 

    def clear_screen(self):
        self.equation=""
        self.screen.configure(state="normal")
        self.screen.delete("1.0",END)

    def insert_screen(self, value,newline=False):
        self.screen.configure(state='normal')
        self.screen.insert(END,value)
        self.equation += str(value)
        self.screen.configure(state ='disabled')


root = Tk()
my_gui = Obliczacz(root)
root.mainloop()
