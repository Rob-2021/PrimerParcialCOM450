def accion(a, b):
    esObligatorio = a
    esDocente = b

    if esObligatorio == "si" and esDocente == True:
        return "actualizar"

print(accion("si", True))