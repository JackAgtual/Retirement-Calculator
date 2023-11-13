from typing import List, Self
from analysis_types import AssumptionsKeys, TradespaceOutput, Assumptions, Metrics, Option, AvailableMetrics
from option_analyzer import OptionAnalyzer
import matplotlib.pyplot as plt


class OptionComparator():
    def __init__(self, options: List[Option], baseline_assumptions: Assumptions):
        self.options = options
        self.baseline_assumptions = baseline_assumptions
    

    def vary(self, variable: AssumptionsKeys, values: List[int | float]) -> Self:
        output: TradespaceOutput = {}

        tradespace: List[Assumptions] = []
        for value in values:
            assumptions = self.baseline_assumptions.copy()
            assumptions[variable] = value
            tradespace.append(assumptions)
        
        for option in self.options:
            name = option['name']
            option_tradespace_output: List[Metrics] = []
            for assumptions in tradespace:
                option_tradespace_output.append(OptionAnalyzer(option, assumptions).metrics())
            output[name] = option_tradespace_output

        self.independent_variable_name = variable
        self.independent_variable_values = values
        self.output = output
        return self


    def plot(self, dependent_var_name: AvailableMetrics) -> None:
        plt.figure()
        for option in self.options:
            option_name = option['name']
            metrics = self.output[option_name]

            metric_vals = []
            for metric in metrics:
                metric_vals.append(metric[dependent_var_name])
            
            plt.plot(self.independent_variable_values, metric_vals, label=option_name, linewidth=2)
        
        plt.xlabel(self.independent_variable_name)
        plt.ylabel(dependent_var_name)
        plt.title(f'{dependent_var_name} vs {self.independent_variable_name}')
        plt.legend()
        plt.show()

            
