import ExtractTickers as et
import yaml
import pandas as pd

# Get all the possible tickers
with open('ChartPatternSuccessRates.yaml', 'r') as f:
    json_data = yaml.safe_load(f)

# Normalise the data in ChartPatternSuccessRates.yaml
success_rate = pd.json_normalize(json_data).transpose()
def parse_percentage_to_int(percentage):
    return float(percentage[:-1])/100
success_rate['success_rate'] = success_rate[0].apply(lambda x: parse_percentage_to_int(x))
column_sum = success_rate['success_rate'].sum()
success_rate['normalised_success_rate'] = success_rate['success_rate'].apply(lambda x: x/column_sum)

# Get the tickers for each chart pattern
tickers = []
for chart_pattern in success_rate.index:
    try:
        tickers.append(et.get_tickers(chart_pattern))
    except Exception as e:
        print(f"Unable to get tickers for {chart_pattern}")