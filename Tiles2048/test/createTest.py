import unittest
import hashlib
import Tiles2048.create as create

class CreateTest(unittest.TestCase):

#  The following is included only for illustrative purposes.  It tests nothing
#  useful.  Please delete and replace with your own test code.

    
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
        
    def test_create_HappyPathTest050(self):
        actualResult = create._create(None)
        encoded = (actualResult['grid'] + '.' + str(actualResult['score'])).encode()
        gridScoreHash = hashlib.sha256(encoded).hexdigest().upper()
        self.assertEqual(actualResult['integrity'], gridScoreHash)
        
    def test_create_SadPathTest060(self):
        actualResult = create._create(None)
        self.assertEqual(actualResult['status'], 'ok')
