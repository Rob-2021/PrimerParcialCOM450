from msilib.schema import Error
import unittest
import obtenerAccion

class TestobtenerAccion(unittest.TestCase):

    def test_prueba1(self):
        self.assertEqual(obtenerAccion.accion("si", True), "actualizar")

    def test_prueba2(self):
        self.assertEqual(obtenerAccion.accion("no", True), "matricular")

    def test_prueba3(self):
        self.assertEqual(obtenerAccion.accion(True, "porConfirmar"), "actualizar")

    def test_prueba4(self):
        self.assertEqual(obtenerAccion.accion(True, "externo"), "registrar")

if __name__ == "__main__":
    unittest.main()