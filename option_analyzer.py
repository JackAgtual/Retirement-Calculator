import numpy as np
import pandas as pd
from analysis_types import Option, Assumptions, Metrics

class OptionAnalyzer():
    def __init__(self, option: Option, assumptions: Assumptions):
        self.option_name = option['name']
        self.your_anual_allowance = option['you'] * 12
        self.benificiary_anual_allowance = option['benificiary'] * 12

        self.your_life_expectancy = assumptions['your_life_expectancy']
        self.benificiary_life_expectancy = assumptions['beneficiary_life_expectancy']
        self.necessary_take_home = assumptions['necessary_take_home'] * 12
        self.stock_market_return = assumptions['stock_market_return']
        self.data = self.__generate_data_table()


    def __generate_data_table(self) -> pd.DataFrame:
        years = np.arange(1, self.benificiary_life_expectancy + 1)
        youre_alive = years <= self.your_life_expectancy
        df = pd.DataFrame(years, columns=['year'])
        
        df['your_income'] = np.where(youre_alive, self.your_anual_allowance, 0)

        remaining_income = self.your_anual_allowance - self.necessary_take_home
        df['your_investment_contribution'] = np.where(
            youre_alive & (df['your_income'] > 0), 
            remaining_income if remaining_income > 0 else 0,
            0
        )

        df['your_take_home'] = df['your_income'] - df['your_investment_contribution']

        investment_val = np.zeros(years.shape)
        for idx, investment_contribution in enumerate(df['your_investment_contribution']):
            if idx == 0:
                investment_val[idx] = investment_contribution
                continue
            investment_val[idx] = (1 + self.stock_market_return) * investment_val[idx - 1] + investment_contribution
        df['investment_value'] = investment_val

        beneficiary_earning_years =  ~youre_alive & (years > self.your_life_expectancy) & (years <= self.benificiary_life_expectancy)
        df['beneficiary_income'] = np.where(beneficiary_earning_years, self.benificiary_anual_allowance, 0)

        return df
    

    def metrics(self) -> Metrics:
        total_investment_contribution = self.data['your_investment_contribution'].sum()
        total_amount_beneficiary_receives_from_pension = self.data['beneficiary_income'].sum()

        # calcualte investment account value at beneficiary eligibility
        investment_val_at_beneficiary_eligibility = self.data.loc[
            (self.data['year'] == self.your_life_expectancy + 1),
            ['investment_value']
        ].iat[0, 0]

        investment_growth = investment_val_at_beneficiary_eligibility - total_investment_contribution

        required_withdraw_rate = self.benificiary_anual_allowance / investment_growth

        return {
            'total_investment_contribution': total_investment_contribution,
            'investment_val_at_beneficiary_eligibility': investment_val_at_beneficiary_eligibility,
            'investment_growth': investment_growth,
            'required_witdraw_rate_to_match_pension': required_withdraw_rate,
            'total_amount_beneficiary_receives_from_pension': total_amount_beneficiary_receives_from_pension
        }

