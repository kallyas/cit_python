import string
import hashlib

"""
1. create your own version of ceaser cipher to output 
any cryptographic code
"""

def ceaser_cipher(text: str, shift: int) -> str:
    """
    :param text: string
    :param shift: int
    :return: string
    """
    # get the alphabet in lowercase
    alphabet = string.ascii_lowercase
    # get the shifted alphabet by slicing the alphabet using the shift
    # and then appending the shifted alphabet to the end of the alphabet
    # e.g. if shift is 2, the shifted alphabet will be 'cdefghijklmnopqrstuvwxyzab'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    # create a translation table using the alphabet and shifted alphabet
    # e.g. if alphabet is 'abcdefghijklmnopqrstuvwxyz' and shifted_alphabet is
    # 'cdefghijklmnopqrstuvwxyzab', the translation table will be
    # {'a': 'c', 'b': 'd', 'c': 'e', 'd': 'f', 'e': 'g', 'f': 'h', 'g': 'i',
    table = str.maketrans(alphabet, shifted_alphabet)
    # return the translated text
    return text.translate(table)


def deciper_ceaser_cipher(text: str, shift: int) -> str:
    """
    :param text: string
    :param shift: int
    :return: string
    """
    # get the alphabet in lowercase
    alphabet = string.ascii_lowercase
    # get the shifted alphabet by slicing the alphabet using the shift
    # and then appending the shifted alphabet to the end of the alphabet
    # e.g. if shift is 2, the shifted alphabet will be 'cdefghijklmnopqrstuvwxyzab'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    # create a translation table using the alphabet and shifted alphabet
    # e.g. if alphabet is 'abcdefghijklmnopqrstuvwxyz' and shifted_alphabet is
    # 'cdefghijklmnopqrstuvwxyzab', the translation table will be
    # {'a': 'c', 'b': 'd', 'c': 'e', 'd': 'f', 'e': 'g', 'f': 'h', 'g': 'i',
    table = str.maketrans(shifted_alphabet, alphabet)
    # return the translated text
    return text.translate(table)


    """
    2. .Create a hash using sha512 algorithm to output a hexidecimal hash.
    """

def hash_sha(text: str) -> str:
        """
        :param text: string
        :return: string
        """
        # create a hash object
        hash_object = hashlib.sha512(text.encode())
        # get the hexadecimal digest of the hash object
        hex_digest = hash_object.hexdigest()
        # return the hexadecimal digest
        return hex_digest


def main():
    # 1. create your own version of ceaser cipher to output
    # any cryptographic code
    text = input('Enter a string: ')
    shift = int(input('Enter a shift: '))
    print(ceaser_cipher(text, shift))

    # verify the ceaser cipher
    print(deciper_ceaser_cipher(ceaser_cipher(text, shift), shift))

    # 2. .Create a hash using sha512 algorithm to output a hexidecimal hash.
    string_to_hash = input('Enter a string to hash: ')
    print(hash_sha(string_to_hash))


if __name__ == '__main__':
    main()