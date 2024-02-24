def fix_caps_lock(word):
    if len(word) == 1:
        return word.upper() if word.islower() else word.lower()
    if word[0].islower() and word[1:].isupper():
        return word.capitalize()
    if word.isupper():
        return word.lower()
    return word


word = input().strip()
print(fix_caps_lock(word))
