def mostrar_bienvenida():
    print("\n===================================")
    print("  Bienvenidos al Torneo de Tenis")
    print("===================================\n")
    print("Hoy tenemos un emocionante partido entre Allan y Carlos.\n")
    print("¡Que comience el juego!\n")

def solicitar_ganador_punto():
    while True:
        try:
            ganador = input("Ingrese el ganador del punto (Allan/Carlos): ").strip().capitalize()
            if ganador not in ["Allan", "Carlos"]:
                raise ValueError("Entrada inválida. Debe ser 'Allan' o 'Carlos'.")
            return ganador
        except ValueError as error:
            print(error)

def actualizar_puntos(puntos, ganador, oponente):
    if puntos[ganador] < 30:
        puntos[ganador] += 15
    elif puntos[ganador] == 30:
        puntos[ganador] = 40
    elif puntos[ganador] == 40 and puntos[oponente] < 40:
        return True  # Ganador del juego
    elif puntos[ganador] == 40 and puntos[oponente] == 40:
        puntos[ganador] = "Advantage"
        puntos[oponente] = "-"
    elif puntos[ganador] == "Advantage" or (puntos[oponente] == "-" and puntos[ganador] == 40):
        return True  # Ganador del juego
    elif puntos[oponente] == "Advantage":
        puntos[oponente] = 40
        puntos[ganador] = 40
    return False

def imprimir_marcador(puntos, juegos, sets):
    puntos_j1 = puntos["Allan"] if puntos["Allan"] != "Advantage" else "Adv"
    puntos_j2 = puntos["Carlos"] if puntos["Carlos"] != "Advantage" else "Adv"
    print("\n--- Estado Actual del Partido ---\n")
    print(f"Puntos Actuales:\n- Allan: {puntos_j1}\n- Carlos: {puntos_j2}")
    print("\nMarcador de Juegos en el Set Actual:")
    print(f"- Allan: {juegos['Allan']}\n- Carlos: {juegos['Carlos']}")
    print("\nMarcador de Sets en el Partido:")
    print(f"- Allan: {sets['Allan']}\n- Carlos: {sets['Carlos']}\n")


def verificar_cambio_cancha(juegos):
    total_juegos = juegos['Allan'] + juegos['Carlos']
    if total_juegos % 2 != 0:
        print("Cambio de cancha.")

def main():
    mostrar_bienvenida()
    juegos = {"Allan": 0, "Carlos": 0}
    sets = {"Allan": 0, "Carlos": 0}
    puntos = {"Allan": 0, "Carlos": 0}

    while sets["Allan"] < 2 and sets["Carlos"] < 2:
        ganador_punto = solicitar_ganador_punto()
        oponente = "Carlos" if ganador_punto == "Allan" else "Allan"
        juego_ganado = actualizar_puntos(puntos, ganador_punto, oponente)
        if juego_ganado:
            juegos[ganador_punto] += 1
            puntos = {"Allan": 0, "Carlos": 0}  # Resetear puntos para el nuevo juego
            verificar_cambio_cancha(juegos)

            # Verificar si un jugador ha ganado el set
            if juegos[ganador_punto] >= 6 and (juegos[ganador_punto] - juegos[oponente]) >= 2:
                sets[ganador_punto] += 1
                juegos = {"Allan": 0, "Carlos": 0}  # Resetear juegos para el nuevo set
                print(f"Set para {ganador_punto}.")

        imprimir_marcador(puntos, juegos, sets)  # Muestra el marcador después de cada punto
        
        if juego_ganado:
            print(f"Punto para {ganador_punto}, gana el juego.")

        if sets["Allan"] == 2 or sets["Carlos"] == 2:
            break  # Finaliza el partido si un jugador gana 2 sets

    ganador_final = "Allan" if sets["Allan"] > sets["Carlos"] else "Carlos"
    print(f"El ganador del partido es {ganador_final} con un marcador final de sets {sets['Allan']}-{sets['Carlos']}.")

if __name__ == "__main__":
    main()
