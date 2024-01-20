r, g, b = map(int, input(", "))


r = max(0, min(r, 255))
g = max(0, min(g, 255))
b = max(0, min(b, 255))

resultado = f"{r:02X}{g:02X}{b:02X}"
print(resultado)
