def crypt (sentence):
    translation=""
    for element in sentence:
        if element in "Aa":
            translation=translation + "1"
        elif element in "Bb":
            translation=translation + "2"
        elif element in "Cc":
            translation=translation + "3"
        elif element in "Dd":
            translation=translation + "4"
        elif element in "Ee":
            translation=translation + "5"
        elif element in "Ff":
            translation=translation + "6"
        elif element in "Gg":
            translation=translation + "7"
        elif element in "Hh":
            translation=translation + "8"
        elif element in "Ii":
            translation=translation + "9"
        elif element in "Jj":
            translation=translation + "a"
        elif element in "Kk":
            translation=translation + "b"
        elif element in "Ll":
            translation=translation + "c"
        elif element in "Mm":
            translation=translation + "d"
        elif element in "Nn":
            translation=translation + "e"
        elif element in "Oo":
            translation=translation + "f"
        elif element in "Pp":
            translation=translation + "g"
        elif element in "Qq":
            translation=translation + "h"
        elif element in "Rr":
            translation=translation + "i"
        elif element in "Ss":
            translation=translation + "j"
        elif element in "Tt":
            translation=translation + "k"
        elif element in "Uu":
            translation=translation + "l"
        elif element in "Vv":
            translation=translation + "m"
        elif element in "Ww":
            translation=translation + "n"
        elif element in "Xx":
            translation=translation + "o"
        elif element in "Yy":
            translation=translation + "p"
        elif element in "Zz":
            translation=translation + ")"
    return translation
print(crypt(input("What do you want to crypt?\n")))

