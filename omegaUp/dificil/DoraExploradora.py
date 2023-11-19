# url: https://omegaup.com/arena/problem/Dora-la-Exploradora-A

MOVIMIENTOS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def explorar_uplandia(n, m, mapa, x_dora, y_dora):
    def dfs(x, y):
        if x < 0 or x >= n or y < 0 or y >= m or mapa[x][y] == '*' or visitado[x][y]:
            return
        visitado[x][y] = True
        mapa[x][y] = '#'
        for dx, dy in MOVIMIENTOS:
            dfs(x + dx, y + dy)

    # Inicializa la matriz de visitados
    visitado = [[False] * m for _ in range(n)]
    # Llama a la función DFS desde la posición de Dora
    dfs(x_dora, y_dora)
    # resultado
    for i in range(n):
        print(''.join(mapa[i]))


# Lectura de la entrada
n, m = map(int, input().split())
mapa = [list(input()) for _ in range(n)]

# Encuentra la posición de Dora
x_dora, y_dora = -1, -1
for i in range(n):
    for j in range(m):
        if mapa[i][j] == '#':
            x_dora, y_dora = i, j

# Llama a la función para explorar UPlandia
explorar_uplandia(n, m, mapa, x_dora, y_dora)
