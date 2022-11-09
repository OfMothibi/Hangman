import hangman
import unittest
from io import StringIO
# from test_base import captured_io

class test_hanging(unittest.TestCase):
    
    def test_hang_display(self):
        # for i in range(8):
        o=hangman.display_hangman(0)
        self.assertEqual(o,""" 
                       
                     |_0_|
                       |
                      / \\
                  
                  
                  """, """Expected a celebrating hangman: (eg)
                       
                     |_0_|
                       |
                      / \\
                  
                  
                  """)
    
if __name__=='__main__':
    unittest.main()
            