import os
import sys
import unittest

class Solution(object):
    def reply(self, value):
        return value

class mytest(unittest.TestCase):  
      
    def setUp(self):  
        self.sol = Solution()  
      
    def tearDown(self):  
        pass  
      
    def test_reply(self):  
        self.assertEqual(self.sol.reply(1), 1, 'test sum fail')  

if __name__ =='__main__':  
    
    unittest.main() 