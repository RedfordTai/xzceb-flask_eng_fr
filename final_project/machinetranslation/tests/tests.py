import unittest

from translator import french_to_english, english_to_french

class Test_frenchToEnglish(unittest.TestCase):
    def test1(self):
        # test null input in frenchToEnglish
        # api return 400
        self.assertEqual(french_to_english(''),"400")

    def test2(self):    
        #test translation of the word 'Bonjour' to 'Hello'
        self.assertEqual(french_to_english('Bonjour'),"Hello")
        
class Test_englishToFrench(unittest.TestCase):
    def test3(self):
        # test null input in englishToFrench
        # api return 400 
        self.assertEqual(english_to_french(''),"400")

    def test4(self):
        #test translation of the word 'Hello' to 'Bonjour'
        self.assertEqual(english_to_french('Hello'),'Bonjour')

unittest.main()