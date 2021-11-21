from random import randint

print("please type the text that you want to encode!")
input = input()
encryptedMessage = ''
errorMessage = ''

for char in input:
    if char == "a" or char == "A":  # Lowercase letters
        number = randint(0, 1)
        if number == 1:
            encryptedMessage = encryptedMessage + "AJ"
        else:
            encryptedMessage = encryptedMessage + "EZ"
    elif char == "b" or char == "B":
        number = randint(0, 1)
        if number == 1:
            encryptedMessage = encryptedMessage + "MN"
        else:
            encryptedMessage = encryptedMessage + "ZY"
    elif char == "c" or char == "C":
        number = randint(0, 1)
        if number == 1:
            encryptedMessage = encryptedMessage + "OQ"
        else:
            encryptedMessage = encryptedMessage + "YM"
    elif char == "d" or char == "D":
        number = randint(0, 1)
        if number == 1:
            encryptedMessage = encryptedMessage + "SV"
        else:
            encryptedMessage = encryptedMessage + "YS"
    elif char == "e" or char == "E":
        number = randint(0, 1)
        if number == 1:
            encryptedMessage = encryptedMessage + "NV"
        else:
            encryptedMessage = encryptedMessage + "YE"
    elif char == "f" or char == "F":
        number = randint(0, 1)
        if number == 1:
            encryptedMessage = encryptedMessage + "TL"
        else:
            encryptedMessage = encryptedMessage + "SA"
    elif char == "g" or char == "G":
        number = randint(0, 1)
        if number == 1:
            encryptedMessage = encryptedMessage + "VX"
        else:
            encryptedMessage = encryptedMessage + "SM"
    elif char == "h" or char == "H":
        number = randint(0, 1)
        if number == 1:
            encryptedMessage = encryptedMessage + "MP"
        else:
            encryptedMessage = encryptedMessage + "JL"
    elif char == "i" or char == "I":
        number = randint(0, 1)
        if number == 1:
            encryptedMessage = encryptedMessage + "MS"
        else:
            encryptedMessage = encryptedMessage + "AA"
    elif char == "j" or char == "J":
        number = randint(0, 1)
        if number == 1:
            encryptedMessage = encryptedMessage + "NT"
        else:
            encryptedMessage = encryptedMessage + "BJ"
    elif char == "k" or char == "K":
        number = randint(0, 1)
        if number == 1:
            encryptedMessage = encryptedMessage + "TQ"
        else:
            encryptedMessage = encryptedMessage + "BL"
    elif char == "l" or char == "L":
        number = randint(0, 1)
        if number == 1:
            encryptedMessage = encryptedMessage + "FP"
        else:
            encryptedMessage = encryptedMessage + "XT"
    elif char == "m" or char == "M":
        number = randint(0, 1)
        if number == 1:
            encryptedMessage = encryptedMessage + "PJ"
        else:
            encryptedMessage = encryptedMessage + "LJ"
    elif char == "n" or char == "N":
        number = randint(0, 1)
        if number == 1:
            encryptedMessage = encryptedMessage + "LO"
        else:
            encryptedMessage = encryptedMessage + "PA"
    elif char == "o" or char == "O":
        encryptedMessage = encryptedMessage + "MX"
    elif char == "p" or char == "P":
        encryptedMessage = encryptedMessage + "SN"
    elif char == "q" or char == "Q":
        encryptedMessage = encryptedMessage + "HV"
    elif char == "r" or char == "R":
        encryptedMessage = encryptedMessage + "KL"
    elif char == "s" or char == "S":
        encryptedMessage = encryptedMessage + "DM"
    elif char == "t" or char == "T":
        encryptedMessage = encryptedMessage + "SK"
    elif char == "u" or char == "U":
        encryptedMessage = encryptedMessage + "MO"
    elif char == "v" or char == "V":
        encryptedMessage = encryptedMessage + "HN"
    elif char == "w" or char == "W":
        encryptedMessage = encryptedMessage + "AP"
    elif char == "x" or char == "X":
        encryptedMessage = encryptedMessage + "AV"
    elif char == "y" or char == "Y":
        encryptedMessage = encryptedMessage + "AD"
    elif char == "z" or char == "Z":
        encryptedMessage = encryptedMessage + "HK"
    elif char == " ":  # Space
        encryptedMessage = encryptedMessage + "UX"
    elif char == "0":  # Numbers
        encryptedMessage = encryptedMessage + "a"
    elif char == "1":
        encryptedMessage = encryptedMessage + "a"
    elif char == "2":
        encryptedMessage = encryptedMessage + "a"
    elif char == "3":
        encryptedMessage = encryptedMessage + "a"
    elif char == "4":
        encryptedMessage = encryptedMessage + "a"
    elif char == "5":
        encryptedMessage = encryptedMessage + "a"
    elif char == "6":
        encryptedMessage = encryptedMessage + "a"
    elif char == "7":
        encryptedMessage = encryptedMessage + "a"
    elif char == "8":
        encryptedMessage = encryptedMessage + "a"
    elif char == "9":
        encryptedMessage = encryptedMessage + "a"
    elif char == ".":
        encryptedMessage = encryptedMessage + "a"
    else:
        errorMessage = errorMessage + "we do not support the character '" + char + "'\n"


if not errorMessage:
    print("\n" + encryptedMessage)
else:
    errorMessage = "There was an error \n" + errorMessage
    print('\n' + errorMessage)
