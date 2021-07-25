from simplificar import somar_fracoes, subtrair_fracoes


class Fracao:

    def __init__(self, numerador, denominador):
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


if __name__ == "__main__":
    print(Fracao(2, 3) + Fracao(2, 3))
    #    4/ 3
    print(sum([Fracao(2, 3), Fracao(2, 3), Fracao(4, 5)]))
    #    32/ 15
    print(Fracao(3, 2) - Fracao(4, 5))
    #    7/ 10




