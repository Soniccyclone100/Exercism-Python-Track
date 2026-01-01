"""Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""



def exchange_money(budget, exchange_rate):
    """
    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """

    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """
    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """

    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """
    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.
    """

    return denomination * number_of_bills


def get_number_of_bills(amount, denomination):
    """
    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    """

    return amount // denomination


def get_leftover_of_bills(amount, denomination):
    """
    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """

    return amount % denomination
    


import math

def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    Calculates the maximum value of foreign currency you can get, rounded down 
    to the nearest whole bill denomination.
    """
    # 1. Calculate the actual exchange rate including the spread fee
    adjusted_rate = exchange_rate * (1 + spread / 100)
    
    # 2. Convert the budget to the total foreign currency amount
    total_foreign_currency = budget / adjusted_rate
    
    # 3. Calculate how many whole bills of the specified denomination fit into that amount
    # Use math.floor to get the integer part
    number_of_bills = math.floor(total_foreign_currency / denomination)
    
    # 4. Calculate the total value those bills represent
    max_exchangeable_value = number_of_bills * denomination
    
    return int(max_exchangeable_value)
