import unittest
import Tiles2048.create as create
from pickle import NONE

class CreateTest(unittest.TestCase):

#  The following is included only for illustrative purposes.  It tests nothing
#  useful.  Please delete and replace with your own test code.

#checks to make sure the size of the string is correct
    def test_create_SadPathTest010(self):
        userParms = {'grid': '0000000000000000', 'score': 15}
        actualResult = create._create(userParms)
        self.assertEqual(actualResult, userParms)
        
    def test_create_SadPathTest020(self):
        userParms = {'grid': '0000000000000000'}
        actualResult = create._create(None)
        self.assertEqual(actualResult['grid'].count('2'), userParms['grid'].count('2'))
        
    def test_create_SadPathTest030(self):
        userParms = {'grid': '0020022000000000'}
        actualResult = create._create(userParms)
        self.assertEqual(actualResult['grid'].count('2'), userParms['grid'].count('2'))
        
    def test_create_SadPathTest040(self):
        actualResult = create._create(None)
        self.assertNotEqual(actualResult['score'], 0)
 
"""       
    def test_create_HappyPathTest010(self):
        userParms = {'grid': '0020020000000000'}
        actualResult = create._create(userParms)
        self.assertEqual(actualResult['grid'].count('2'), userParms['grid'].count('2'))
        
    
    def test_create_HappyPathTest020(self):
        numOfTwos = 2
        actualResult = create._create(None)
        self.assertEqual(numOfTwos, actualResult['grid'].count('2'))
        
    def test_create_HappyPathTest030(self):
        sizeOfGrid = 16
        actualResult = create._create(None)
        self.assertEqual(sizeOfGrid, len(actualResult['grid']))
        
    def test_create_HappyPathTest040(self):
        actualResult = create._create(None)
        self.assertEqual(actualResult['score'], 0)
"""