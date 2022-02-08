import unittest
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import translator
from translator import english_to_french, french_to_english


class TestenglishToFrench(unittest.TestCase): 
    def test1(self): 
        
       #First test
       inputText = english_to_french('What is your name?')
       expected = 'Quel est votre nom?'
       self.assertEqual(inputText, expected)

       #Second test
       inputText = english_to_french('I love you ')
       expected =  "Je t'aime "
       self.assertEqual(inputText, expected)

       #Hello test
       inputText = english_to_french('hello')
       expected = 'Bonjour'
       self.assertEqual(inputText, expected)
       
       # Null test
       inputText = english_to_french('None')
       expected =  ''
       self.assertNotEqual(inputText, expected)

       inputText2 = english_to_french(0)
       expected2 =  0
       self.assertNotEqual(inputText2, expected2)


    
class TestfrenchToEnglish(unittest.TestCase): 
    def test1(self): 
       
       #First test
       inputText = french_to_english('Puis-je avoir des directions?')
       expected =  'Can I have directions?'
       self.assertEqual(inputText, expected)

       #Second test
       inputText = french_to_english("J’aime aller à la plage")
       expected = 'I like going to the beach'
       self.assertEqual(inputText, expected)

       #Hello test
       inputText = french_to_english('Bonjour')
       expected = 'Hello'
       self.assertEqual(inputText, expected)
       
       # Null test
       inputText = french_to_english('None')
       expected =  ''
       self.assertNotEqual(inputText, expected)

       inputText2 = french_to_english(0)
       expected2 =  0
       self.assertNotEqual(inputText2, expected2)

       
       
unittest.main()

