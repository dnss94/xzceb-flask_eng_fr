import unittest

from translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase):
    def test1(self):
         self.assertEqual(english_to_french('Hello'), 'Bonjour')
         self.assertNotEqual(english_to_french('Hello'), 'Hello')
         self.assertNotEqual(english_to_french("None"), '')
         self.assertNotEqual(english_to_french(0), 0)


class TestF2E(unittest.TestCase):
    def test2(self):
         self.assertEqual(french_to_english('Bonjour'), 'Hello')
         self.assertNotEqual(french_to_english('Bonjour'), 'Benjour')
         self.assertNotEqual(french_to_english("None"), '')
         self.assertNotEqual(french_to_english(0), 0)
unittest.main()