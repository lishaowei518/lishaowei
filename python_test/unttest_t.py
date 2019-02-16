# -*- coding: utf-8 -*-
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.number=raw_input('enter a number')
        self.number=int(self.number)
    
    def test_case1(self):
        print self.number
        self.assertEquals(self.number, 10, msg='your input is not 10')
    
    def test_case2(self):
        print self.number
        self.assertEqual(self.number, 20, msg='your input is not 20')
        
    
    @unittest.skip('暂时跳过用例3的测试')
    def test_case3(self):
        print self.number
        self.assertEqual(self.number, 30, msg='Your input is not 30')
    
    
    def tearDown(self):
        print 'Test over'

if __name__=='_main_':
    unittest.main()