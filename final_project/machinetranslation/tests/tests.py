"""System module."""
import unittest
from ../translator import translate_english_to_french, translate_french_to_english

class Testf2e(unittest.TestCase):
    """ Testf2e """
    def test_1(self):
        ''' test_1 '''
        self.assertEqual(translate_french_to_english('0'), '0')
        self.assertEqual(translate_french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(translate_french_to_english("None"), '')
        self.assertNotEqual(translate_french_to_english(0), 0)


class Teste2f(unittest.TestCase):
    """ Teste2f """
    def test_1(self):
        ''' test_1 '''
        self.assertEqual(translate_english_to_french('0'), '0')
        self.assertEqual(translate_english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(translate_english_to_french("None"), '')
        self.assertNotEqual(translate_english_to_french(0), 0)

unittest.main()