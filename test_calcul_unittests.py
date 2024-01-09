import unittest

#_______________________________ IMPORTER LA CLASSE A TESTER
from calcul import *

#_______________________________ CREATION DE LA CLASSE DE TEST (hérite de unittest.TestCase)
class TestCalcul(unittest.TestCase):
    
    # Configuration nécessaire avant chaque test (pour factoriser, en créant à chaque fois un nouvel objet, ici self.calc). 
    # SetUp dépend de la classe unittest.
    def setUp(self):
        self.calc = Calcul()
    
    # Test Addition
    def test_additionner(self):
        resultat = self.calc.additionner(3, 5)
        # Vérifier si le résultat est égal à 8
        self.assertEqual(resultat, 8)
    
    # Test Soustraction
    def test_soustraire(self):
        resultat = self.calc.soustraire(10, 4)
        self.assertEqual(resultat, 6)
    
    # Test Multiplication 
    def test_multiplier(self):
        resultat = self.calc.multiplier(10, 4)
        self.assertEqual(resultat, 40)
    # Test Division
    def test_diviser(self):
        resultat = self.calc.diviser(10, 4)
        self.assertEqual(resultat, 2.5)
    
    # Test Division par 0
    def test_division_zero(self):
        resultat = self.calc.diviser(10, 0)
        self.assertEqual(resultat, "Division par zéro impossible")
        # with self.assertRaises(ZeroDivisionError, msg="Division par zéro impossible"):
        #     self.calc.diviser(5, 0)
    
# Exécuter les tests si le script est exécuté directement
if __name__ == '__main__':
    unittest.main()