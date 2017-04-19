class Polinomio:
    def __init__(self):
        self.polinomio = []

    def append(self, monom):
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
        index = 0
        for monom in self.polinomio:
            if monom.variavel is not None:
                if target in monom.variavel or monom.variavel is None:
                    monom.raiseExp(target)
            else:
                self.polinomio[index] = None
            index += 1

        self.polinomio = filter(lambda x: x is not None, self.polinomio)

    def deriva(self, target):
        pass

    def __iter__(self):
        return self.polinomio.__iter__()

    def __next__(self):
        return self.polinomio.__next__()

    @property
    def __len__(self):
        return self.polinomio.__len__()