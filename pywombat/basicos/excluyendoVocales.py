def excludes_vowel_counter(cadena: str) -> int:
    cantidad = 0
    for char in cadena:
        if char in ('a', 'e', 'i', 'o', 'u', ' '):
            continue
        cantidad += 1
    return cantidad


if __name__ == "__main__":
    cadena = input().lower()
    print(excludes_vowel_counter(cadena))
