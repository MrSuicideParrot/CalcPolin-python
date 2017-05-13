from tkinter import *
from tkinter import messagebox

from pyparsing import Word, nums, alphas,Or, OneOrMore, Suppress, Optional
from polinomio import Polinomio, Monomio

class rootWindow:
    def __init__(self, master):

        self.last = None
        '''Definições'''

        '''Labels'''
        self.lab4 = Label(master, text='Eq1')
        self.lab5 = Label(master, text='Eq2')
        self.lab6 = Label(master, text='Solução')

        '''Entries'''
        self.entrEq1 = Entry(master, justify=CENTER)


        self.entrEq2 = Entry(master, justify=CENTER)


        self.entrSol = Label(master, justify=CENTER, text='')

        self.entrDer = Entry(master, justify=CENTER,width = 5)
        self.entrDer.grid(row=1, column = 5)

        self.entrInt = Entry(master, justify=CENTER,width = 5)
        self.entrInt.grid(row=2, column = 5)

        self.butDer = Button(root, text='Derivar', width=12, command=self.deriva).grid(row=1, column=4)
        self.butInt = Button(root, text='Integrar', width=12, command=self.integra).grid(row=2, column=4)
        self.butNor = Button(root, text='Normalizar', width=18, command=self.normaliza).grid(row=3, column=4,columnspan = 2)
        self.butCop = Button(root, text='Somar', width=18, command=self.somar).grid(row=4, column=4, columnspan = 2)

        self.flag = False
        self.R1 = Button(root, text='Utilizar último valor cálculado', state=DISABLED, command=self.changeState)
        self.R1.grid(row=3,columnspan=4)



        self.lab4.grid(row=1)
        self.lab5.grid(row=2)
        self.lab6.grid(row=4)

        self.entrEq1.grid(row=1, column=1, columnspan=3)
        self.entrEq2.grid(row=2, column=1, columnspan=3)
        self.entrSol.grid(row=4, column=1, columnspan=3)

    @staticmethod
    def entryParser(entry):
        """
        :param entry: Entrada que pretende fazer parser
        :type entry: Entry
        """
        expressao = Polinomio()
        monomio1 = Word(nums)
        monomio2 = Word(nums)+Suppress('*')+Word(alphas)+Suppress('^')+Word(nums)
        parser = monomio2^monomio1 +Optional(Suppress('+'))
        aux = OneOrMore(parser).parseString(entry.get())

        i = 0  # type i: int
        while (i<len(aux)):
            try:
                if aux[i].isdigit() and aux[i+1] in alphas and aux[i+2].isdigit():
                        expressao.append(Monomio(int(aux[i]), aux[i+1],int(aux[i+2])))
                        i += 3
                elif aux[i].isdigit():
                        expressao.append(Monomio(int(aux[i])))
                        i += 1
                else:
                    raise ValueError
            except IndexError: #apanha o erro de quando temos um algarismo como ultima posição
                try:
                    if aux[i].isdigit():
                        expressao.append(Monomio(int(aux[i])))
                        i += 1
                    else:
                        raise ValueError
                except:
                    raise ValueError


        return expressao

    def getOneEntry(self):
        if self.entrEq1.get() is not '':
            return self.entryParser(self.entrEq1)
        elif self.entrEq2.get() is not '':
            return self.entryParser(self.entrEq2)
        else:
            return None

    def deriva(self):
        if not self.flag:
            try:
                polin = self.getOneEntry()
            except:
                messagebox.showerror('Equação inválida', 'Erro de síntaxe!')
                return

            if polin is None:
                messagebox.showerror('Equação inválida','Não se encontra nenhuma função!')
                return
        else:
            polin = self.last

        if self.entrDer.get() is '':
            messagebox.showerror('Variável inválida','Não se encontra nenhuma variável!')
            return

        polin.deriva(self.entrDer.get())
        self.last = polin
        self.entrSol.config(text=polin.__str__())
        #self.flag = False

        '''Verificação para saber se pode ou não permitir que a função seje voltada a usar
        no caso de ela tiver duas variaveis não pode ser voltada a utilizar
        '''
        f1 = True
        for aux in polin:
            if aux.aux is not None:
                f1 = False
        if f1:
            self.R1.config(state=ACTIVE)
        else:
            self.R1.config(state=DISABLED)

    def integra(self):
        if not self.flag:
            try:
                polin = self.getOneEntry()
            except:
                messagebox.showerror('Equação inválida', 'Erro de síntaxe!')
                return

            if polin is None:
                messagebox.showerror('Equação inválida','Não se encontra nenhuma função!')
                return
        else:
            polin = self.last

        if self.entrInt.get() is '':
            messagebox.showerror('Variável inválida','Não se encontra nenhuma variável!')
            return

        polin.integra(self.entrInt.get())
        self.last = polin
        self.entrSol.config(text=polin.__str__())
        #self.flag = False

        '''Verificação para saber se pode ou não permitir que a função seje voltada a usar
        no caso de ela tiver duas variaveis não pode ser voltada a utilizar
        '''
        f1 = True
        for aux in polin:
            if aux.aux is not None:
                f1 = False
        if f1:
            self.R1.config(state=ACTIVE)
        else:
            self.R1.config(state=DISABLED)

    def somar(self):
        try:
            polin1 = self.entryParser(self.entrEq1)
            polin2 = self.entryParser(self.entrEq2)
        except:
            messagebox.showerror('Equação inválida', 'Não se encontra uma das funções ou erro de síntax!')
            return

        polin1.sum(polin2)
        self.entrSol.config(text=polin1.__str__())

    def normaliza(self):
        if not self.flag:
            polin = self.getOneEntry()

            if polin is None:
                messagebox.showerror('Equação inválida','Não se encontra nenhuma função!')
                return
        else:
            polin = self.last

        polin.normalisa()
        self.entrSol.config(text=polin.__str__())
        self.R1.config(state=ACTIVE)

    def changeState(self):
        self.entrEq1.delete(0, 'end')
        self.entrEq1.insert(0,self.last)

root = Tk()
root.title('Calculadora de Polinómios')
hey = rootWindow(root)

root.mainloop()