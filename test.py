from app import app
import unittest

class FlaskTestCase(unittest.TestCase):
    
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertTrue(b'Hello, world!' in response.data)
        
 
if __name__ == '__main__':
    unittest.main()