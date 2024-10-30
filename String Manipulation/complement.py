"""
File: complement.py
Name: Jason
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    """
    Change DNA to NEW , A to T; T to A; G to C; C to G
    """
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    new = ""
    if dna == '':
        return "DNA strand is missing."
    else:
        for i in range(len(dna)):
            ch = dna[i]
            if ch == 'A':
                new = new + 'T'
            elif ch == 'T':
                new = new + 'A'
            elif ch == 'G':
                new = new + 'C'
            else:
                new = new + 'G'
        return new


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
