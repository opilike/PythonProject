"""
File: name_sq.py (extension)
Name: Jason
----------------------------
This program is an extension of assignment3!
It will ask the user to provide a name, 
and the square pattern of the given name 
will be printed on the console.
"""


def main() :
    """
    square pattern of the given name
    """
    pass
    print("This program prints a name in a squarepattern!")
    name = input("Name: ")
    s_name(name)


def s_name(name):
    new = name
    for i in range(len(new)):
        if i == 0:
            print(str(new))
        elif i == (len(new)-1):
            for j in range(len(new)):
                last = ""
                last = last+new[len(new)-1-j]
                print(str(last), end="")
        else:
            print(new[i], end="")
            for k in range(len(new)-2):
                print(" ", end="")
            print(str(new[len(new)-i]))


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
