import collections as col
import functools 
import typing as typ



def remover_elem_comuns(array1: list, array2: list) -> typ.Tuple[list, list]:
    """Remove elementos comuns entre dois arrays"""
    counter_1 = col.Counter(array1)
    counter_2 = col.Counter(array2)

    new_array_1 = list((counter_1 - counter_2).elements())
    new_array_2 = list((counter_2 - counter_1).elements())

    return new_array_1 or [1], new_array_2 or [1]



def decomposicao(numero: int) -> list:
    """Decompõe um número nos seus fatores mínimos"""

    fatores = []

    for i in range(2, numero+1):
        while numero % i == 0:
            numero /= i
            fatores.append(i) 
    
    return fatores


def simplificar(numerador: int, denominador: int) -> typ.Tuple[int, int]:
    """Simplifica uma função"""
    if numerador == denominador:
        return 1

    # Flags para permitir valores negativos
    # No caso de numerador e denominador negativos, o menos é excluído
    if numerador < 0 and not denominador < 0:
        num_e_neg = True 
    else:
        num_e_neg = False


    if denominador < 0 and not numerador < 0:
        den_e_neg = True 
    else:
        den_e_neg = False
        
    
    fat_num = decomposicao(abs(numerador))
    fat_den = decomposicao(abs(denominador))

    fat_num, fat_den = remover_elem_comuns(fat_num,  fat_den)

    new_num = functools.reduce(lambda num1, num2: num1 * num2, fat_num)
    new_den = functools.reduce(lambda num1, num2: num1 * num2, fat_den)

    return -new_num if num_e_neg else new_num, -new_den if den_e_neg else new_den


def soma_fracoes(numerador1, denominador1, numerador2, denominador2):
    """Soma frações e depois aplica simplificação"""
    novo_num = numerador1 * denominador2 + numerador2 * denominador1
    novo_den = denominador1 * denominador2
    return simplificar(novo_num, novo_den)

def subtracao_fracoes(numerador1, denominador1, numerador2, denominador2):
    """Subtrai frações e depois aplica simplificação"""
    novo_num = numerador1 * denominador2 - numerador2 * denominador1
    novo_den = denominador1 * denominador2
    return simplificar(novo_num, novo_den)