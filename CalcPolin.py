from tkinter import *

class rootWindow:
    def __init__(self, master):

        '''Definições'''

        '''Labels'''
        self.lab1 = Label(master, text='Coeficiente')
        self.lab2 = Label(master, text='Variável')
        self.lab3 = Label(master, text='Expoente')
        self.lab4 = Label(master, text='Eq1')
        self.lab5 = Label(master, text='Eq2')
        self.lab6 = Label(master, text='Solução')

        '''Entries'''
        self.entrCoe1 = Entry(master, justify=CENTER)
        self.entrVar1 = Entry(master, justify=CENTER)
        self.entrExp1 = Entry(master, justify=CENTER)

        self.entrCoe2 = Entry(master, justify=CENTER)
        self.entrVar2 = Entry(master, justify=CENTER)
        self.entrExp2 = Entry(master, justify=CENTER)

        self.entrCoe3 = Entry(master, justify=CENTER, state='disabled')
        self.entrVar3 = Entry(master, justify=CENTER, state='disabled')
        self.entrExp3 = Entry(master, justify=CENTER, state='disabled')

        self.butDer = Button(root, text='Derivar', width=12, command=self.deriva).grid(row=1, column=4)
        self.butInt = Button(root, text='Integrar', width=12).grid(row=2, column=4)
        self.butNor = Button(root, text='Normalizar', width=12).grid(row=3, column=4)
        self.butCop = Button(root, text='Somar', width=12).grid(row=4, column=4)

        self.flag = False
        R1 = Radiobutton(root, text='Utilizar último valor cálculado', state=DISABLED, variable=self.flag, value=True).grid(row=3,columnspan=4)

        self.lab3.grid(column=3)

        self.lab4.grid(row=1)
        self.lab5.grid(row=2)
        self.lab6.grid(row=4)

        self.lab1.grid(column=1, row=0)
        self.entrCoe1.grid(row=1, column=1)
        self.entrCoe2.grid(row=2, column=1)
        self.entrCoe3.grid(row=4, column=1)

        self.lab2.grid(column=2, row=0)
        self.entrVar1.grid(row=1, column=2)
        self.entrVar2.grid(row=2, column=2)
        self.entrVar3.grid(row=4, column=2)

        self.lab3.grid(column=3, row=0)
        self.entrExp1.grid(row=1, column=3)
        self.entrExp2.grid(row=2, column=3)
        self.entrExp3.grid(row=4, column=3)

    def deriva(self):
        pass




root = Tk()
root.title('Calculadora de Polinómios')
hey = rootWindow(root)

root.mainloop()