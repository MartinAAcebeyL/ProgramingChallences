def quien_gano(flix, martontito):
    if flix == martontito:
        return "EMPATE"
    elif flix == "4":
        return "FLIX"
    elif flix == "0" and martontito =="2":
        return "FLIX"
    elif flix == "5" and martontito =="0":
        return "FLIX"
    elif flix == "2" and martontito =="5":
        return "FLIX"
    else:
        return "MARTONTITO"


a, b = input().split()
print(quien_gano(a, b))
