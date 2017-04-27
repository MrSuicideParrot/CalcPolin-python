class Monomio:
    def __init__(self, coeficiente, variavel=None, expoente=None):
        self.coeficiente = coeficiente
        self.variavel = variavel
        self.expoente = expoente
        self.aux = None

    '''Derivar monómio'''
    def decreasesExp(self):
        if self.expoente == 1:
            self.variavel = None
            self.expoente = None
        elif self.expoente == 0:
            return True  # e necessário eliminar
        else:
            self.coeficiente *= self.expoente
            self.expoente -= 1
        return False

    '''Integrar monómio'''
    def raiseExp(self, target):
        if self.variavel is None:
            self.variavel = target
            self.expoente = 1
        elif target  in self.variavel:
            self.expoente += 1
            self.coeficiente /= self.expoente
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


class Polinomio:
    """
    :type polinomio: list[Monomio]
    """
    def __init__(self):
        self.polinomio = []

    def append(self, monom):
        """
        :param monom: Monómio que pretende fazer input
        :type monom: Monomio
        """
        self.polinomio.append(monom)

    def normalisa(self):
        aux = []
        index = 0
        for i1 in range(len(self.polinomio)):
            if self.polinomio[i1] is not None:
                aux.append(self.polinomio[i1])
                for i2 in range(i1+1, len(self.polinomio)):
                    if self.polinomio[i1].similar(self.polinomio[i2]):
                        aux[index].coeficiente += self.polinomio[i2].coeficiente
                        self.polinomio[i2] = None
                index += 1

        self.polinomio = aux

    def integra(self, target):
        '''
        :param target: Variável ao qual pretende integrar
        :type target: str
        '''
        self.normalisa()
        for monom in self.polinomio:
            monom.raiseExp(target)

    def sum(self, p2):
        """
        :param p2: Segunda equação
        :type p2: Polinomio
        """
        p1 = self
        p1.normalisa()
        p2.normalisa()
        aux = []

        for x1 in range(len(p1)):
            aux.append(Monomio(self.polinomio[x1].coeficiente, self.polinomio[x1].variavel, self.polinomio[x1].expoente))
            for x2 in range(x1+1, len(p2)):
                if self.polinomio[x1].variavel == self.polinomio[x2].variavel and self.polinomio[x1].expoente == self.polinomio[x2].expoente:
                    self.aux[x1].coeficiente += self.polinomio[x2].coeficiente
                    break

        self.polinomio = aux

    def deriva(self, target):
        '''
         :param target: Variável ao qual pretende derivar
         :type target: str
         '''
        self.normalisa()
        for x1 in range(len(self.polinomio)):
            if target in self.polinomio[x1].coeficiente or self.polinomio[x1].coeficiente is None:
                resultado = self.polinomio[x1].decreasesExp()
                if resultado:
                    self.polinomio[x1] = None

        self.polinomio = filter(lambda x: x is not None, self.polinomio)


    def __iter__(self):
        return self.polinomio.__iter__()

    def __next__(self):
        return self.polinomio.__next__()

    @property
    def __len__(self):
        return self.polinomio.__len__()


def main():
    """ Função para testes"""
    pass

if __name__ == '__main__':
    main()
