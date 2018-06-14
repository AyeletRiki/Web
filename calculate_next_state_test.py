import unittest
from web_calculator import calculate_next_state

class TestCalculateNextState(unittest.TestCase):
    
    def test_plus(self):
        s = None
        s = calculate_next_state(s, '1')
        self.assertEqual(s['display'], '1')
        s = calculate_next_state(s, '2')
        self.assertEqual(s['display'], '12')
        s = calculate_next_state(s, '+')
        self.assertEqual(s['display'], '12')
        s = calculate_next_state(s, '1')
        self.assertEqual(s['display'], '1')
        s = calculate_next_state(s, '3')
        self.assertEqual(s['display'], '13')
        s = calculate_next_state(s, '=')
        self.assertEqual(s['display'], '25')

    def test_minus(self):
        s = None
        s = calculate_next_state(s, '1')
        self.assertEqual(s['display'], '1')
        s = calculate_next_state(s, '2')
        self.assertEqual(s['display'], '12')
        s = calculate_next_state(s, '-')
        self.assertEqual(s['display'], '12')
        s = calculate_next_state(s, '1')
        self.assertEqual(s['display'], '1')
        s = calculate_next_state(s, '3')
        self.assertEqual(s['display'], '13')
        s = calculate_next_state(s, '=')
        self.assertEqual(s['display'], '-1')

    def test_mult(self):
        s = None
        s = calculate_next_state(s, '1')
        self.assertEqual(s['display'], '1')
        s = calculate_next_state(s, '2')
        self.assertEqual(s['display'], '12')
        s = calculate_next_state(s, '*')
        self.assertEqual(s['display'], '12')
        s = calculate_next_state(s, '1')
        self.assertEqual(s['display'], '1')
        s = calculate_next_state(s, '3')
        self.assertEqual(s['display'], '13')
        s = calculate_next_state(s, '=')
        self.assertEqual(s['display'], '156')

    def test_div(self):
        s = None
        s = calculate_next_state(s, '2')
        self.assertEqual(s['display'], '2')
        s = calculate_next_state(s, '2')
        self.assertEqual(s['display'], '22')
        s = calculate_next_state(s, '/')
        self.assertEqual(s['display'], '22')
        s = calculate_next_state(s, '1')
        self.assertEqual(s['display'], '1')
        s = calculate_next_state(s, '1')
        self.assertEqual(s['display'], '11')
        s = calculate_next_state(s, '=')
        self.assertEqual(s['display'], '2')

    def test_equal(self):
        s = None
        s = calculate_next_state(s, '=')
        self.assertEqual(s['display'], '')
        s = calculate_next_state(s, '2')
        self.assertEqual(s['display'], '2')
        s = calculate_next_state(s, '=')
        s = calculate_next_state(s, '5')
        self.assertEqual(s['display'], '5')

    def test_complex(self):
        s = None
        s = calculate_next_state(s, '1')
        self.assertEqual(s['display'], '1')
        s = calculate_next_state(s, '2')
        self.assertEqual(s['display'], '12')
        s = calculate_next_state(s, '+')
        self.assertEqual(s['display'], '12')
        s = calculate_next_state(s, '1')
        self.assertEqual(s['display'], '1')
        s = calculate_next_state(s, '3')
        self.assertEqual(s['display'], '13')
        s = calculate_next_state(s, '*')
        self.assertEqual(s['display'], '25')
        s = calculate_next_state(s, '4')
        self.assertEqual(s['display'], '4')
        s = calculate_next_state(s, '/')
        self.assertEqual(s['display'], '100')
        s = calculate_next_state(s, '2')
        self.assertEqual(s['display'], '2')
        s = calculate_next_state(s, '-')
        self.assertEqual(s['display'], '50')
        s = calculate_next_state(s, '10')
        self.assertEqual(s['display'], '10')
        s = calculate_next_state(s, '=')
        self.assertEqual(s['display'], '40')
# main
if __name__ == '__main__':
    unittest.main()