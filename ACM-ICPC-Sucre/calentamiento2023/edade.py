def calcular_edad(fecha_nacimiento: list, fecha: list) -> int:
    """
    fecha_nacimiento: lista con tres elementos, el primer elemento es el dia, el segundo es el mes y el tercero es el año
    fecha: lista con tres elementos, el primer elemento es el dia, el segundo es el mes y el tercero es el año
    """
    dia_nacimiento, mes_nacimiento, anio_nacimiento = fecha_nacimiento
    dia, mes, anio = fecha
    edad = anio - anio_nacimiento
    if mes_nacimiento > mes:
        edad -= 1
    elif mes_nacimiento == mes:
        if dia_nacimiento > dia:
            edad -= 1
    return edad


if __name__ == "__main__":
    fecha_nacimiento = list(map(int, input().split()))
    fecha = list(map(int, input().split()))
    print(calcular_edad(fecha_nacimiento, fecha))
