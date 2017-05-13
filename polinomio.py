class Monomio:
    """
    :type coeficiente: int
    :type variavel: str
    :type expoente: int
    
    """
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
        elif self.expoente == 0 or self.expoente is None:
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
            self.coeficiente = self.coeficiente/self.expoente
        else:
            self.aux = target


    def similar(self, t2):
        if t2 is None:
            return False

        t1 = self
        if (t1.variavel == t2.variavel) and (t1.expoente == t2.expoente):
            return True
        else:
            return False

    def __str__(self):
        if self.variavel is not None:
            if self.aux is None:
                return str(self.coeficiente)+'*'+self.variavel+'^'+str(self.expoente)
            else:
                return str(self.coeficiente) + '*' +self.aux+'*'+self.variavel + '^' + str(self.expoente)
        else:
            return str(self.coeficiente)
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

        for x1 in range(len(p1.polinomio)):
            aux.append(Monomio(p1[x1].coeficiente, p1[x1].variavel, p1[x1].expoente))
            for x2 in range(len(p2.polinomio)):
                if p2[x2] is not None and p1[x1].variavel == p2[x2].variavel and p1[x1].expoente == p2[x2].expoente:
                    aux[x1].coeficiente += p2[x2].coeficiente
                    p2[x2] = None
                    break

        p2.polinomio = list(filter(lambda x: x is not None, p2))
        self.polinomio = aux + p2.polinomio

    def deriva(self, target):
        '''
         :param target: Variável ao qual pretende derivar
         :type target: str
         '''
        self.normalisa()
        for x1 in range(len(self.polinomio)):
            #teste = self.polinomio[x1].variavel == target
            if self.polinomio[x1].variavel == target  or self.polinomio[x1].variavel is None:
                resultado = self.polinomio[x1].decreasesExp()
                if resultado:
                    self.polinomio[x1] = None

        self.polinomio = list(filter(lambda x: x is not None, self.polinomio))


    def __iter__(self):
        return self.polinomio.__iter__()

    def __next__(self):
        return self.polinomio.__next__()

    def __getitem__(self, item):
        return self.polinomio[item]

    def __setitem__(self, key, value):
        self.polinomio[key] = value

    @property
    def __len__(self):
        return self.polinomio.__len__()

    def __str__(self):
        res = ''
        if self.polinomio:
            res = self.polinomio[0].__str__()

            for aux in self.polinomio[1:]:
                res = res + '+' + aux.__str__()

        return res



def main():
    """ Função para testes"""
    pass

if __name__ == '__main__':
    main()
