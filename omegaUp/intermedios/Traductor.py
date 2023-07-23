# url: https://omegaup.com/arena/problem/traductor/

if __name__ == "__main__":
    string = input()
    char1 = string.split("?")[0]
    char2, char3 = string.split("?")[1].split(":")

    string = f"if({char1})\n\t{char2};\nelse\n\t{char3};"
    print(string)
