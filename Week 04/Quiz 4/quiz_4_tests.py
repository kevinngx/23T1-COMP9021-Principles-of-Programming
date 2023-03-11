import unittest
from quiz_4 import is_good_prime, good_primes

class GoodPrimesTest(unittest.TestCase):
    def test_is_good_prime(self):
        self.assertTrue(is_good_prime(5))
        self.assertTrue(is_good_prime(17))
        self.assertFalse(is_good_prime(24))

    def test_good_primes(self):
        self.assertEqual(['7'], good_primes('_7'))
        self.assertEqual(['10', '17'], good_primes('1__7'))
        self.assertEqual(['10', '17', '23', '29', '31'], good_primes('1__723493'))

if __name__ == '__main__':
    unittest.main()