# url: https://leetcode.com/problems/valid-word/description/


def isValid(word: str) -> bool:
    config = {
        "min_size": False,
        "has_english_letters": False,
        "has_a_vowel": False,
        "has_a_constant": False,
        "donsent_has_a_especial_letter": True,
    }
    if len(word) >= 3:
        config["min_size"] = True

    vowels = "aeiouAEIOU"
    for caracter in word:
        if caracter.isalnum():
            config["has_english_letters"] = True
            if caracter in vowels:
                config["has_a_vowel"] = True
            elif caracter.isalpha():
                print("caracter: ",caracter)
                config["has_a_constant"] = True
        else:
            config["donsent_has_a_especial_letter"] = False
    print(config)
    especial_letter = config.pop("donsent_has_a_especial_letter")
    print(sum(config.values()))
    return especial_letter and sum(config.values()) >= 4

# print(isValid("aya"))
# print(isValid("234Adas"))
# print(isValid("b3"))
# print(isValid("a3$e"))
print(isValid("UuE6"))
