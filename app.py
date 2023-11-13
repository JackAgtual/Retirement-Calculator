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
    market_return_trade.plot('investment_val_at_beneficiary_eligibility')
    market_return_trade.plot('required_witdraw_rate_to_match_pension')
    


if __name__ == '__main__':
    main()