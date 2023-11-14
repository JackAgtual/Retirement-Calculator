from typing import List
from analysis_types import Option
import json
from assumptions import assumptions
from option_comparator import OptionComparator
import numpy as np

def main():
    with open('data.json', 'r') as file:
        options: List[Option] = json.load(file)
    
    market_return_trade = OptionComparator(options, assumptions)\
        .vary('stock_market_return', np.linspace(0.02, 0.1, 100))
    market_return_trade.plot('effective_total_income')

    withdraw_rate_trade = OptionComparator(options, assumptions)\
        .vary('investment_withdraw_rate', np.linspace(0.025, 0.1, 100))
    withdraw_rate_trade.plot('effective_total_income')

    necessary_take_home_trade = OptionComparator(options, assumptions)\
        .vary('necessary_take_home', np.linspace(6000, 12000, 100))
    necessary_take_home_trade.plot('effective_total_income')


if __name__ == '__main__':
    main()