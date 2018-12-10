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
    # TODO: read from the csv and populate a dictionary

    # TODO: return the dictionary

    # TODO: remove this "return None" statement when complete
    return None

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
    # TODO: find all the tax brackets that the individual agi "hits"

    # TODO: determine how much of each tax bracket the individual agi "hits"

    # TODO: calculate amount of tax owed per tax bracket

    # TODO: sum the tax owed

    # TODO: return total tax owed

    # TODO: remove the following "return -1" when code is complete
    return -1
