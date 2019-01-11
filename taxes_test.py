import unittest
import os
from taxes import build_tax_dictionary, calculate_tax


# The preparation of constants to use in the test case

MY_DIR = os.path.dirname(os.path.realpath(__file__))
TAX_RATE_FILENAME = 'income_tax_rates_2018.csv'

TAX_RATE_DICT = build_tax_dictionary(MY_DIR + '/' + TAX_RATE_FILENAME)


# dictionary to hold gross and expected result
GROSS_TAX_DICT = {
    75_000: 9_997,
    50_000: 4_497,
    120_000: 20_657,
    82_000: 11_537,
    250_000: 59_237,
    550_000: 165_757
}
# 165_567
MY_STANDARD_DEDUCTION = 12_000

class TestTaxes(unittest.TestCase):
    """
    test class
    """
    def do_compare(self, index):
        """
        generic compare method to be used by each
        individual test case
        """
        my_gross = list(GROSS_TAX_DICT.keys())[index]
        my_expected_tax_owed = GROSS_TAX_DICT[my_gross]
        my_agi = my_gross - MY_STANDARD_DEDUCTION
        my_tax_owed = calculate_tax(my_agi, TAX_RATE_DICT)
        self.assertEqual(my_tax_owed, my_expected_tax_owed)

    def test_do_test_75000(self):
        self.do_compare(0)

    def test_do_test_50000(self):
        self.do_compare(1)

    def test_do_test_120000(self):
        self.do_compare(2)

    def test_do_test_82000(self):
        self.do_compare(3)

    def test_do_test_250000(self):
        self.do_compare(4)

    def test_do_test_550000(self):
        self.do_compare(5)


if __name__ == '__main__':
    unittest.main()
