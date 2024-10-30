"""
File: similarity.py (extension)
Name: Jason
----------------------------
This program is an extension of assignment3!
It will compare short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    make ls be DNA search and ss is DNA for match
    """
    # Make Long sequence and short sequence
    ls = (input("Please give me a DNA sequence to search: "))
    ss = (input("What DNA sequence would you like to match? "))
    match(ls, ss)


def match(ls, ss):
    ss = ss.upper()
    ls = ls.upper()
    #  count is count match associative property
    #  count2 is second match associative property
    count = 0
    count2 = 0
    #  make match_s is final output
    match_s = ""
    for i in range(len(ls)-len(ss)+1):
        #  make match_s2 is inside compare string
        match_s2 = ""
        for j in range(len(ss)):
            if ss[j] == ls[i + j]:
                count2 += 1
        if count2 > count:
            for k in range(i, i + len(ss)):
                match_s2 += ls[k]
            count = count2
            match_s = match_s2
            #  make inside counter initial to be 0 and ""
            count2 = 0
    print("The best match is "+str(match_s))


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
