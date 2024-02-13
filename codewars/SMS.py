# url: https://www.codewars.com/kata/535a69fb36973f2aad000953

from typing import Union


sms = "No one expects the Spanish Inquisition! Our chief weapon is surprise, fear and surprise; two chief weapons, fear, surprise, and ruthless efficiency! And that will be it."


def capitalize(sms: Union[str, list[str]]) -> str:
    """Capitaliza todo el mensaje."""
    if isinstance(sms, str):
        str_list = sms.split(" ")
        return "".join(map(lambda char: char.capitalize(), str_list))
    return "".join(map(lambda char: char.capitalize(), sms))


def shortener(sms: str):
    list_sms = sms.split(" ")
    MAX_SIZE = 160
    sms_size = len(sms)

    if sms_size <= MAX_SIZE:
        """cuando el sms es del tamanio adecuado, no se hace nada."""
        return sms
    amount_white_space = sms_size - len(list_sms)
    if sms_size - amount_white_space > MAX_SIZE:
        """cuando el mensaje es muy largo, tanto que quitando los espacios no se puede reducir a 160 caracteres. Se devuelve el mensaje sin espacios y capitalizado."""
        print(1)
        return "".join(list_sms).capitalize()
    else:
        """cuando el mensaje es muy largo, pero quitando los espacios se puede reducir a 160 caracteres."""
        print(2)
        print(amount_white_space)
        print(len(list_sms))

        r = " ".join(list_sms[:-amount_white_space])
        print(r)
        r += "".join(list_sms[amount_white_space:]).capitalize()
        return r


print(shortener(sms))

# No one expects the Spanish Inquisition! Our chief weapon is surprise, fear and surprise; two chief weapons, fear,Surprise,AndRuthlessEfficiency!AndThatWillBeIt.
