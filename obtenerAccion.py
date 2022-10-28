def accion(a, b):
    esObligatorio = a
    esDocente = b

    if esObligatorio == "si" and esDocente == True:
        return "actualizar"

    if esObligatorio == "no" and esDocente == True:
        return "matricular"

print(accion("si", True))