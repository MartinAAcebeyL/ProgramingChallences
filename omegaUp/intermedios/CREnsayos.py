# url: https://omegaup.com/arena/problem/CR-Ensayos/#

def arreglar_ensayo(ensayo: str) -> str:
    ensayo = ensayo.lower()
    ensayo = ensayo[0].upper()+ensayo[1:]

    for i in range(1, len(ensayo)-1):
        if ensayo[i] in '!.':
            ensayo = ensayo[:i+2]+ensayo[i+2].upper()+ensayo[i+3:]

    return ensayo


if __name__ == "__main__":
    ensayo = input()
    print(arreglar_ensayo(ensayo))
