from re import A


def accion(a, b):
    esObligatorio = a
    esDocente = b
    esExterno = a
    estadoRegistro = b

    if esObligatorio == "si" and esDocente == True:
        return "actualizar"

    if esObligatorio == "no" and esDocente == True:
        return "matricular"

    if esExterno == True and estadoRegistro == "porConfirmar":
        return "actualizar"

print(accion("si", True))