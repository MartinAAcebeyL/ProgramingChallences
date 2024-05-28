# url: https://leetcode.com/problems/goat-latin/description/


def toGoatLatin(self, sentence: str) -> str:
    def start_consonant(word: str, i: int) -> str:
        return "".join([word[1:], word[0], "ma", "a" * i])

    def start_vowel(word: str, i: int) -> str:
        return "".join([word, "ma", "a" * i])

    vowels = set("aeiouAEIOU")
    words = sentence.split()
    n = len(words)
    new_sentence = [""] * n
    for i in range(n):
        word = words[i]
        if word[0] in vowels:
            new_sentence[i] = start_vowel(word, i + 1)
        else:
            new_sentence[i] = start_consonant(word, i + 1)
    return " ".join(new_sentence)


print(toGoatLatin("I speak Goat Latin"))
# Imaa peaksmaaa oatGmaaaa atinLmaaaaa
# Imaa peaksmaaa oatGmaaaa atinLmaaaaa

print(toGoatLatin("The quick brown fox jumped over the lazy dog"))
# heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa
# heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa
