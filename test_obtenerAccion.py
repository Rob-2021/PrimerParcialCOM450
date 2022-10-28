from msilib.schema import Error
import unittest
import obtenerAccion

class TestobtenerAccion(unittest.TestCase):

    def test_prueba1(self):
        self.assertEqual(obtenerAccion.accion("si", True), "actualizar")

    def test_prueba2(self):
        self.assertEqual(obtenerAccion.accion("no", True), "matricular")

if __name__ == "__main__":
    unittest.main()