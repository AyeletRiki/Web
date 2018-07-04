import unittest, requests, json

class TestCalculatorServer(unittest.TestCase):

    def test_null(self):
        response = requests.post('http://127.0.0.1:3000/calculate', json={'calculatorState': None, 'input': '1'})
        response_content = json.loads(response.content)
        self.assertEqual(response_content['display'], '1')
        self.assertEqual(response_content['num1'], '1')
        self.assertEqual(response_content['num2'], '')
        self.assertEqual(response_content['operator'], '')

    def test_complex(self):
        response = requests.post('http://127.0.0.1:3000/calculate', json={'calculatorState': None, 'input': '1'})
        s = json.loads(response.content)
        response = requests.post('http://127.0.0.1:3000/calculate', json={'calculatorState': s, 'input': '2'})
        s = json.loads(response.content)
        response = requests.post('http://127.0.0.1:3000/calculate', json={'calculatorState': s, 'input': '+'})
        s = json.loads(response.content)
        response = requests.post('http://127.0.0.1:3000/calculate', json={'calculatorState': s, 'input': '1'})
        s = json.loads(response.content)
        response = requests.post('http://127.0.0.1:3000/calculate', json={'calculatorState': s, 'input': '3'})
        s = json.loads(response.content)
        response = requests.post('http://127.0.0.1:3000/calculate', json={'calculatorState': s, 'input': '/'})
        s = json.loads(response.content)
        response = requests.post('http://127.0.0.1:3000/calculate', json={'calculatorState': s, 'input': '5'})
        s = json.loads(response.content)
        response = requests.post('http://127.0.0.1:3000/calculate', json={'calculatorState': s, 'input': '='})
        s = json.loads(response.content)
        self.assertEqual(s['display'], '5')

# main
if __name__ == '__main__':
    unittest.main()