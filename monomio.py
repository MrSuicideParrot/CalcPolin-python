class Monomio:
    def __init__(self, coeficiente, variavel=None, expoente=None):
        self.coeficiente = coeficiente
        self.variavel = variavel
        self.expoente = expoente
        self.aux = None

    def decreasesExp(self):
        if self.expoente == 1:
            self.variavel = None
            self.expoente = None
        elif self.expoente == 0:
            return True  # e necessário eliminar
        else:
            self.expoente -= 1
        return False

    def raiseExp(self, target):
        if self.variavel is None:
            self.variavel = target
            self.expoente = 1
        elif target  in self.variavel:
            self.expoente += 1
        else:
            self.aux = target


    def similar(self, t2):
        if t2 is None:
            return False

        t1 = self
        if (t1.coeficiente == t2.coeficiente) and (t1.expoente == t2.expoente):
            return True
        else:
            return False

    def __str__(self):
        if self.variavel is not None:
            return str(self.coeficiente)+'*'+self.variavel+str(self.expoente)