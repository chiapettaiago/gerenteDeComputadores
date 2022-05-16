from functools import cache


class Computadores:
    def __init__(self, os, processador, memoria, idade, utilizador):
        self.os = os
        self.processador = processador
        self.memoria = memoria
        self.idade = idade
        self.utilizador = utilizador