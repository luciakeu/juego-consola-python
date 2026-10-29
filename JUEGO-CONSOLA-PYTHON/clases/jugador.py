import random


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self.salud = 100
        self.experiencia = 0

    def atacar(self):
        return random.randint(10, 20) * self.nivel

    def recibir_dano(self, dano):
        self.salud -= dano
        if self.salud <= 0:
            return f"{self.nombre} ha sido derrotado."
        return f"Recibiste {dano} de daño. Tu salud actual es: {self.salud}"

    def ganar_experiencia(self, experiencia):

        self.experiencia += experiencia
        if self.experiencia >= 100:
            self.nivel += 1
            self.experiencia = 0
            print(f"{self.nombre} ha subido al nivel {self.nivel}!")