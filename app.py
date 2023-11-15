from typing import List
from analysis_types import Option
import json
from assumptions import baseline_assumptions
from option_analyzer import OptionAnalyzer
from option_comparator import OptionComparator
import matplotlib.pyplot as plt
import numpy as np

def main():
    with open('data.json', 'r') as file:
        options: List[Option] = json.load(file)
    
    market_return_trade = OptionComparator(options, baseline_assumptions)\
        .vary('stock_market_return', np.linspace(0.02, 0.1, 100))
    market_return_trade.plot('effective_total_income')

    withdraw_rate_trade = OptionComparator(options, baseline_assumptions)\
        .vary('investment_withdraw_rate', np.linspace(0.025, 0.1, 100))
    withdraw_rate_trade.plot('effective_total_income')

    necessary_take_home_trade = OptionComparator(options, baseline_assumptions)\
        .vary('necessary_take_home', np.linspace(8000, 12000, 100))
    necessary_take_home_trade.plot('effective_total_income')

    your_life_expectancy_trade = OptionComparator(options, baseline_assumptions)\
        .vary('your_life_expectancy', np.arange(20, 40, 1))
    your_life_expectancy_trade.plot('effective_total_income')

    # Total effective income vs necessary take home & withdrawal rate
    necessary_take_home_vals = np.linspace(8000, 12000, 10)
    withdraw_rate_vals = np.linspace(0.03, 0.1, 5)
    effective_incomes = []
    min_effective_income = np.inf
    max_effective_income = -1 * np.inf
    
    for option in options:
        effective_income = np.empty((len(withdraw_rate_vals),len(necessary_take_home_vals)))
        for i, withdraw_rate in enumerate(withdraw_rate_vals):
            for j, take_home in enumerate(necessary_take_home_vals):
                assumptions = baseline_assumptions.copy()
                assumptions['necessary_take_home'] = take_home
                assumptions['investment_withdraw_rate'] = withdraw_rate
                cur_effective_income = OptionAnalyzer(option, assumptions).metrics()['effective_total_income']
                effective_income[i][j] = cur_effective_income

                if cur_effective_income > max_effective_income:
                    max_effective_income = cur_effective_income
                if cur_effective_income < min_effective_income:
                    min_effective_income = cur_effective_income
        
        effective_incomes.append(effective_income)

    
    _, axes = plt.subplots(1, len(options))
    for option_cnt, (ax, option, effecive_income_matrix) in enumerate(zip(axes, options, effective_incomes), start=1):
        ax.set_title(f'Effective beneficiary income\n{option['name']}')
        plt.subplot(1, len(options), option_cnt)
        for withdraw_rate_idx, effective_income in enumerate(effecive_income_matrix):
            withdraw_rate = round(withdraw_rate_vals[withdraw_rate_idx] * 1000) / 10
            plt.plot(necessary_take_home_vals, effective_income, label=f'{withdraw_rate}%', linewidth=2)
            plt.legend(title='Withdrawal rate')
            plt.ylim(min_effective_income, max_effective_income)
            plt.ylabel('Effective beneficiary income')
            plt.xlabel('Necessary take home pay')
    
    plt.show()

if __name__ == '__main__':
    main()