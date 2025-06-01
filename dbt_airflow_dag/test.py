from typing import Self

class Car:
    def __init__(self, brand: str, horsepower: int) -> None:
        self.brand = brand
        self.horsepower = horsepower

    def __str__(self) -> str:
        return f'{self.brand} car with {self.horsepower} horsepower'

    def __add__(self, other: Self) -> str:
        return f'{self.brand} & {other.brand} cars have a combined horsepower of {self.horsepower + other.horsepower}'
    
volvo: Car = Car('Volvo', 200)
mercedes: Car = Car('Mercedes', 300)
print(volvo + mercedes)  # Output: Volvo & Mercedes cars have a combined horsepower of 500
print(volvo) # Output: Volvo car with 200 horsepower

a = 5
b = 10
def add(a: int, b: int) -> int:
    return a + b
print(add(a, b))  # Output: 15


entrada = ['PaTiNeTe', 'SKATE', 'pATINete', 'BicicletA']

def seq_string(entrada:list) -> dict:

    saida = {}

    for i in entrada:
        lower_case = i.lower()
        if lower_case not in saida.keys():
            saida[lower_case] = 1
        else:
            saida[lower_case] += 1
            

    return saida

print(seq_string(entrada))  # Output: {'patinete': 2, 'skate': 1, 'bicicleta': 1}


