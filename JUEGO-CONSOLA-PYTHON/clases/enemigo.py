import random


class Enemigo:
    def __init__(self, nombre, salud, dano):
        self.nombre = nombre
        self.salud = salud
        self.dano = dano

    def atacar(self):
        return random.randint(5, 15) * self.dano

    def recibir_dano(self, dano):
        self.salud -= dano
        if self.salud <= 0:
            return f"{self.nombre} ha sido derrotado."
        else:
            return f"{self.nombre} ha recibido {dano} de daño. Salud restante: {self.salud}"