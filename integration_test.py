import urllib
import unittest, requests

class TestCalculatorServer(unittest.TestCase):

    def test_null(self):
        response = requests.post('http://127.0.0.1:3000/calculate', data={'calculatorState': None, 'input': '1'})
        self.assertEqual(response['display'], '1')
        self.assertEqual(response['num1'], '1')
        self.assertEqual(response['num2'], '')
        self.assertEqual(response['operator'], '')

    # def test_complex(self):



# main
if __name__ == '__main__':
    unittest.main()