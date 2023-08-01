

if __name__ == "__main__":
    jugadas = input()
    juego = [True, False, False]

    for jugada in jugadas:
        if jugada == "A":
            juego[0], juego[1] = juego[1], juego[0]
        elif jugada == "B":
            juego[1], juego[2] = juego[2], juego[1]
        else:
            juego[0], juego[2] = juego[2], juego[0]

    index = juego.index(True)
    print(index+1)
