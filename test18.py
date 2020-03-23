import unittest



class TestModuloMethod(unittest.TestCase):
    """
    Test the modulo_method
    """
    def test_add_integers(self):
        """
        Test that the addition of two integers returns the correct total
        """
        result = mymath.add(1, 2)
        self.assertEqual(result, 3)




if __name__ == '__main__':
    unittest.main()
