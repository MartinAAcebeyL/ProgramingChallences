# url:https://omegaup.com/arena/problem/Watermel/
def dividir_sandia(peso):
    if peso % 2 != 0 or peso == 2:
        return "NO"
    return "SI"


peso_sandia = int(input())
resultado = dividir_sandia(peso_sandia)
print(resultado)
