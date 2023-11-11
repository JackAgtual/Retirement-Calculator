from typing import List
from analysis_types import Option
import json
from assumptions import assumptions
from option_analyzer import OptionAnalyzer

def main():
    with open('data.json', 'r') as file:
        options: List[Option] = json.load(file)
    
    option_analyzer = OptionAnalyzer(options[1], assumptions)
    metrics = option_analyzer.metrics()
    print(metrics)


if __name__ == '__main__':
    main()