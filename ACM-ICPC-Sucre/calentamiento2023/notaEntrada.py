PORCENTAJE_LABORATORIO = 0.25
PORCENTAJE_TAREAS = 0.1
PORCENTAJE_EXAMEN_PARCIAL = 0.3
PORCENTAJE_EXAMEN_FINAL = 0.35


def calcular_minima_nota(nl: float, t: float, ep: float) -> float:
    """
    nl: nota laboratorio
    t: nota de tareas
    ep: nota de examen parcial
    """
    nota_entrada = nl * PORCENTAJE_LABORATORIO + t * \
        PORCENTAJE_TAREAS + ep * PORCENTAJE_EXAMEN_PARCIAL
    para_aprobar = 51 - nota_entrada
    return round(nota_entrada, 1), round(para_aprobar, 1)


if __name__ == "__main__":
    datos = []
    for _ in range(3):
        datos.append(float(input()))

    nota_entrada, minima_nota = calcular_minima_nota(*datos)
    print(f"Entrada = {nota_entrada}\nMinimo = {minima_nota}")
