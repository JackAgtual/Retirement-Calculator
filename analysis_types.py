from typing import TypedDict, Literal, List, Union

class Option(TypedDict):
    name: str
    you: float
    benificiary: float

class Assumptions(TypedDict):
    your_life_expectancy: int
    beneficiary_life_expectancy: int
    stock_market_return: float
    necessary_take_home: int
    investment_withdraw_rate: float

AssumptionsKeys = Literal[
    'your_life_expectancy',
    'beneficiary_life_expectancy',
    'stock_market_return',
    'necessary_take_home',
    'investment_withdraw_rate'
]

class Metrics(TypedDict):
    total_investment_contribution: float
    investment_val_at_beneficiary_eligibility: float
    investment_growth: float
    required_witdraw_rate_to_match_pension: float
    total_amount_beneficiary_receives_from_pension: float
    effective_investment_income: float
    effective_total_income: float

AvailableMetrics = Literal[
    'total_investment_contribution',
    'investment_val_at_beneficiary_eligibility',
    'investment_growth',
    'required_witdraw_rate_to_match_pension',
    'total_amount_beneficiary_receives_from_pension',
    'effective_investment_income',
    'effective_total_income'
]

class TradespaceOutput(TypedDict):
    option:  List[Metrics]