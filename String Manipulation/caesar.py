"""
File: caesar.py
Name: Jason
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    give a number how to shift
    and give a ciphered string
    out put deciphered string!
    """
    number = input('Secret number: ')
    ciphered_s = input("What's the ciphered string? ")
    new_a = shift(ALPHABET, number, ciphered_s)
    print('The deciphered string is: ' + str(new_a))


def shift(old_a, number, s):
    #  make a new_ALPHABET
    new_a = ''
    counter = len(old_a)-int(number)
    new_a += old_a[counter:]
    counter = len(old_a)-int(number)
    new_a += old_a[:counter]
    ans = ''
    #  make input ciphered string upper all ch
    s = s.upper()
    #  check input ciphered string ch location in old ALPHABET and make deciphered string!
    for ch in s:
        i = new_a.find(ch)
        if i == -1:
            ans += ch
        else:
            ans += ALPHABET[i]
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
