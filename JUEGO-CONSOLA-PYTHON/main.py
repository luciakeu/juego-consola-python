import random

from clases.enemigo import Enemigo
from clases.jugador import Jugador


def main():
    nombre_jugador = input(
        "¡Bienvenido a la aventura en el Espacio! Por favor, ingrese su nombre: "
    )

    jugador = Jugador(nombre_jugador)

    enemigos = [
        Enemigo("Alien", 50, 2),
        Enemigo("Robot", 80, 3),
        Enemigo("Monstruo", 60, 4),
    ]

    enemigos_derrotados = []

    print("Comienza la Aventura!!")

    while True:
        enemigo_actual = random.choice(enemigos)
        if enemigo_actual in enemigos_derrotados:
            continue
        print(f"Te encuentras con un {enemigo_actual.nombre} con {enemigo_actual.salud} de salud, en tu camino.")

        while enemigo_actual.salud > 0 and jugador.salud > 0:
            accion = input(
                "¿Qué deseas hacer? (atacar / huir): "
            ).lower()

            if accion == "atacar":
                dano_jugador = jugador.atacar()
                print(f"Has atacado al {enemigo_actual.nombre} causando {dano_jugador} de daño.")
                print(f"--> La salud actual del enemigo es: {enemigo_actual.salud} <--")
                print()
                resultado_enemigo = enemigo_actual.recibir_dano(dano_jugador)
                print(resultado_enemigo)

                if enemigo_actual.salud > 0:
                    dano_enemigo = enemigo_actual.atacar()
                    print(f"El {enemigo_actual.nombre} te ha atacado causando {dano_enemigo} de daño.")
                    print(f"--> Tu salud actual es: {jugador.salud} <--")
                    resultado_jugador = jugador.recibir_dano(dano_enemigo)
                    print(resultado_jugador)

            elif accion == "huir":
                print("Has decidido huir. ¡Hasta la próxima aventura!")
                break
            else:
                print("Acción no válida. Por favor, elige 'atacar' o 'huir'.")


        if jugador.salud <= 0:
            print("Has sido derrotado. GAME OVER.")
            break

        if enemigo_actual.salud <= 0:
            print(f"¡Felicidades! Has derrotado al {enemigo_actual.nombre}.")
            enemigos_derrotados.append(enemigo_actual)
            enemigos.remove(enemigo_actual)

        jugador.ganar_experiencia(20)

        continuar = input("¿Deseas continuar la aventura? (si / no): ").lower()
        if continuar != "si":
            print("Gracias por jugar. ¡Hasta la próxima aventura!")
            break

    if not enemigos:
        print("¡Felicidades! Has derrotado a todos los enemigos. ¡Eres un héroe del Espacio!")

if __name__ == "__main__":
    main()