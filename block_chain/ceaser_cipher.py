# create a ceaser cipher

import string


def ceaser_cipher(text: str, shift: int) -> str:
    """
    :param text: string
    :param shift: int
    :return: string
    """
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return text.translate(table)

def deciper_ceaser_cipher(text: str, shift: int) -> str:
    """
    :param text: string
    :param shift: int
    :return: string
    """
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(shifted_alphabet, alphabet)
    return text.translate(table)


if __name__ == '__main__':
    text = input('Enter a string: ')
    shift = int(input('Enter a shift: '))
    print(ceaser_cipher(text, shift))
    print(deciper_ceaser_cipher(ceaser_cipher(text, shift), shift))