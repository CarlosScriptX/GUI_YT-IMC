from tkinter import*
import tkinter as tk



app = Tk()
app.geometry("500x600")

def buttonDestroy():
    global botao2
    botao2.destroy()

def buttonTwo():
    global botao2
    botao2.pack()


botao = Button(app,text='ok',command=buttonTwo)
botao.place(x=200,y=60)

botao2 = Button(app,text='destroy',command=buttonDestroy)

app.mainloop()



