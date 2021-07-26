from simplificar import *


class Fracao:

    def __init__(self, numerador, denominador=1):
        if denominador == 0:
            raise ValueError("O denominador não pode ser zero.")

        self.numerador = numerador 
        self.denominador = denominador
        

    def __str__(self):
        return f"{self.numerador}/ {self.denominador}"

    def __repr__(self):
        return f"{self.numerador}/ {self.denominador}"

    def __add__(self, fracao2):
        return Fracao(*somar_fracoes(self.numerador, self.denominador, fracao2.numerador, fracao2.denominador))

    def __radd__(self, fracao2):
        if fracao2 == 0:
            return self
        else:
            return self.__add__(fracao2)

    def __sub__(self, fracao2):
        return Fracao(*subtrair_fracoes(self.numerador, self.denominador, fracao2.numerador, fracao2.denominador))

    def __mul__(self, fracao2):
        return Fracao(*simplificar(self.numerador * fracao2.numerador, self.denominador * fracao2.denominador))

    def __rmul__(self, fracao2):
        if fracao2 == 1:
            return self
        else:
            return self.__mul__(fracao2)

    # __truediv__ para "/" -> sem simplificação; __floordiv__ para "//" -> com simplificação
    def __truediv__(self, fracao2):
        return Fracao(self.numerador * fracao2.denominador, self.denominador * fracao2.numerador)

    def __floordiv__(self, fracao2):
        return Fracao(*simplificar(self.numerador * fracao2.denominador, self.denominador * fracao2.numerador))


if __name__ == "__main__":
    print(Fracao(2, 3) + Fracao(3, 2))
    # 13/ 6
    print(sum([Fracao(2, 3), Fracao(2, 3), Fracao(4, 5)]))
    # 32/ 15
    print(Fracao(3, 2) - Fracao(4, 5))
    # 7/ 10
    print(Fracao(1, 2) * Fracao(3, 2) * Fracao(6, 7) * Fracao(9, 3))
    # 27/ 14
    print(Fracao(100) * Fracao(99, 2))
    # 4950/ 1
    print(Fracao(5, 4) / Fracao(2, 7) / Fracao(4, 7) / Fracao(1, 3) / Fracao(1, 2))
    # 735/ 16
