# url: https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python
def make_dictionary_characters(string: str) -> dict:
    dictionary = {}
    for character in string:
        dictionary[character] = dictionary.get(character, 0) + 1
    return dictionary


def make_new_string(old_string: str, dictionary: dict):
    new_string = ""
    for character in old_string:
        if dictionary.get(character) == 1:
            new_string += "("
            continue
        new_string += ")"

    return new_string


string = input()
dictionary = make_dictionary_characters(string)
print(make_new_string(string, dictionary))
