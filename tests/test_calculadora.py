import unittest

from calculadora import soma


class TestCalculadora(unittest.TestCase):
    def test_soma_5_e_5_deve_retornar_10(self):
        self.assertEqual(soma(5, 5), 10)

    def test_soma_5_negativo_e_5_deve_retornar_0(self):
        self.assertEqual(soma(-5, 5), 0)

    def test_soma_multiple_ins(self):
        x_y_outs = (
            (10, 10, 20),
            (5, 5, 10),
            (1.5, 1.5, 3),
            (-5, 5, 0),
            (100, 100, 200)
        )

        for x_y_out in x_y_outs:
            with self.subTest(x_y_out=x_y_out):
                x, y, out = x_y_out
                self.assertEqual(soma(x, y), out)

    def test_soma_x_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma('11', 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
