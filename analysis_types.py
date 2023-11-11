from typing import TypedDict

class Option(TypedDict):
    name: str
    you: float
    benificiary: float

class Assumptions(TypedDict):
    your_life_expectancy: int
    beneficiary_life_expectancy: int
    stock_market_return: float
    necessary_take_home: int

class Metrics(TypedDict):
    total_investment_contribution: float
    investment_val_at_beneficiary_eligibility: float
    investment_growth: float
    required_witdraw_rate_to_match_pension: float
    total_amount_beneficiary_receives_from_pension: float
