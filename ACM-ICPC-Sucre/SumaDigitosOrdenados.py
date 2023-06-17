if __name__ == "__main__":
    numeros = list(map(int, input().split('+')))
    numeros.sort()
    suma = sum(numeros)

    numeros_str = [str(numero) for numero in numeros]
    resultado = "+".join(numeros_str)
    print(f"{resultado}={suma}")
