import csv
import os

def build_tax_dictionary(filename):
    """
    Take in the filename of the taxrates,
    which is ordered as follows :
        Percent rate, start of bracket, end of bracket, range of bracket
    return the dictionary
    NOTES:
    (a) The key for the dictionary should probably be the start of the bracket
    (b) You may do additional computations and add those to the dictionary.
    (c) For instance, calculating the total tax paid for a bracket
    (range * percent rate) would be a useful value to have in the dictionary
    """
    dict = {}

    with open(filename, 'r') as f:
        csv_file = csv.reader(f)
        next(csv_file)

        for row in csv_file:
            key = int(row[1])

            rate = float(row[0])
            low = int(row[1])
            high = int(row[2])
            delta = int(row[3])

            value = (rate, low, high, delta)

            dict[key]=value

        return(dict)

def calculate_tax(agi, tax_dict):
    """
    The agi is adjust gross income (int) that reflects the taxable
    income after any deductions and adjustments.  We use this to determine
    what the tax payer's tax rate is.

    The tax_dict is a dictionary of tax rates and the range

    return the amount of the tax as an INT (round down/truncate)

    KEY NOTE :
    a taxpayer pays tax rates in EACH of the brackets up to his current one
    and only pays the part of his income that falls in the top tax bracket

    eg., if a person's agi is $50,000
    then s/he pays :
        10% for $9,525 (full amount of 10% tax bracket)
        + 12% for $29,175 (full amount of 12% tax bracket)
        + 22% for $22,200 (amount of $50,000 - $37,800 that falls in 22% tax bracket)

    s/he does NOT pay 22% of $50,000!!
    """
    keys = len(tax_dict.keys())
    keys_for_dict = list(tax_dict.keys())

    pay = 0


    for i in range(keys):
        rate = tax_dict[keys_for_dict[i]][0]
        low = tax_dict[keys_for_dict[i]][1]
        high = tax_dict[keys_for_dict[i]][2]
        delta = tax_dict[keys_for_dict[i]][3]

        if agi > high:
            pay = rate*delta + pay
            pass
        else:
            pay = rate*(agi - low) + pay
            return(int(pay))



# MY_DIR = os.path.dirname(os.path.realpath(__file__))
# TAX_RATE_FILENAME = 'income_tax_rates_2018.csv'
#
# TAX_RATE_DICT = build_tax_dictionary(MY_DIR + '/' + TAX_RATE_FILENAME)
# print(TAX_RATE_DICT)



# print(calculate_tax(550_000-12000, TAX_RATE_DICT))
