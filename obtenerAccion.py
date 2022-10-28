from re import A


def accion(a, b):
    esObligatorio = a
    esDocente = b
    esExterno = a
    estadoRegistro = b
    tipoPersonaDestino = b

    if esObligatorio == "si" and esDocente == True:
        return "actualizar"
    else:
    # if esObligatorio == "no" and esDocente == True:
        return "matricular"

    if esExterno == True and estadoRegistro == "porConfirmar":
        return "actualizar"

    if esExterno == True and tipoPersonaDestino == externo:
        return "registrar"

print(accion("si", True))