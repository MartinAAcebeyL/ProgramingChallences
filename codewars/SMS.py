# url: https://www.codewars.com/kata/535a69fb36973f2aad000953

from typing import List

MAX_SIZE = 160
sms = (
    "SMS messages are limited to 160 characters. It tends to be irritating, "
    "especially when freshly written message is 164 characters long. "
    "SMS messages are limited to 160 characters. It tends to be irritating, "
    "especially when freshly written message is 164 characters long."
)


def capitalize(sms: List[str]) -> str:
    """Capitaliza todo el mensaje."""
    return "".join(
        map(lambda char: char if char[0].isupper() else char.capitalize(), sms)
    )


def shortener(sms: str):
    sms_size = len(sms)

    if sms_size <= MAX_SIZE:
        """cuando el sms es del tamanio adecuado, no se hace nada."""
        return sms
    list_sms = sms.split(" ")
    white_space = sms.count(" ")
    if sms_size - white_space > MAX_SIZE:
        """cuando el mensaje es muy largo, tanto que quitando los espacios no se puede reducir a 160 caracteres. Se devuelve el mensaje sin espacios y capitalizado."""
        return capitalize(list_sms)
    else:
        """cuando el mensaje es muy largo, pero quitando los espacios se puede reducir a 160 caracteres."""
        index = sms_size - MAX_SIZE
        r = " ".join(list_sms[:-index])
        r += capitalize(list_sms[-(index):])
        return r


print(shortener(sms))
