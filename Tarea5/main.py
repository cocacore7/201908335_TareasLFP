cadena = "__servidor1"
cadena2 = "3servidor"


def afd(entrada):
    estado = 0
    for letra in entrada:
        if estado == 0:
            if letra == "-":
                estado = 1
            elif letra == "a" or letra == "b" or letra == "c" or letra == "d" or letra == "e" or letra == "f" or \
                    letra == "g" or letra == "h" or letra == "i" or letra == "j" or letra == "k" or letra == "l" or \
                    letra == "m" or letra == "n" or letra == "o" or letra == "p" or letra == "q" or letra == "r" or \
                    letra == "s" or letra == "t" or letra == "u" or letra == "v" or letra == "w" or letra == "x" or \
                    letra == "y" or letra == "z":
                estado = 2
            else:
                print("Cadena Incorrecta ---Error---")
                return
        elif estado == 1:
            if letra == "-":
                estado = 1
            elif letra == "a" or letra == "b" or letra == "c" or letra == "d" or letra == "e" or letra == "f" or \
                    letra == "g" or letra == "h" or letra == "i" or letra == "j" or letra == "k" or letra == "l" or \
                    letra == "m" or letra == "n" or letra == "o" or letra == "p" or letra == "q" or letra == "r" or \
                    letra == "s" or letra == "t" or letra == "u" or letra == "v" or letra == "w" or letra == "x" or \
                    letra == "y" or letra == "z":
                estado = 3
            else:
                print("Cadena Incorrecta ---Error---")
                return
        elif estado == 2:
            if letra == "a" or letra == "b" or letra == "c" or letra == "d" or letra == "e" or letra == "f" or \
                    letra == "g" or letra == "h" or letra == "i" or letra == "j" or letra == "k" or letra == "l" or \
                    letra == "m" or letra == "n" or letra == "o" or letra == "p" or letra == "q" or letra == "r" or \
                    letra == "s" or letra == "t" or letra == "u" or letra == "v" or letra == "w" or letra == "x" or \
                    letra == "y" or letra == "z":
                estado = 2
            elif letra == 0 or letra == 1 or letra == 2 or letra == 3 or letra == 4 or letra == 5 or letra == 6 or \
                    letra == 7 or letra == 8 or letra == 9:
                estado = 4
            else:
                print("Cadena Incorrecta ---Error---")
                return
        elif estado == 3:
            if letra == 0 or letra == 1 or letra == 2 or letra == 3 or letra == 4 or letra == 5 or letra == 6 or \
                    letra == 7 or letra == 8 or letra == 9:
                estado = 4
            else:
                print("Cadena Incorrecta ---Error---")
                return
        elif estado == 4:
            print("Cadena Aceptada :D")
        else:
            print("Cadena Incorrecta")


afd(cadena)
afd(cadena2)
