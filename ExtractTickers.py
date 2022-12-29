import yaml
from bs4 import BeautifulSoup
import cloudscraper

"""
    # This is a quick function to get the chart patterns from finviz
   
    # Constraints:
        # The function is slow as I set it to sleep as the api has a limit of 5 calls per minute
        # Speeding it up requires a paid subscription to the api
        # Call this function to get the tickers with the respective chart patterns
        # The available chart patterns are in finviz_chart_patterns.yaml 
        
        # The alpha vantage api is not able to recognise alot of company names. However, this serves our purposes still
        # as we do not need everything lmao
        
    # Example:
        # import ExtractTickers as et 
        # tickers = et.get_tickers("Wedge")
        # tickers should return tickers with the wedge chart pattern
"""
def get_tickers(desired_chart_pattern):

    finviz_url = "https://finviz.com/screener.ashx?v=210&s="
    with open("finviz_chart_patterns.yaml", "r") as stream:
        chart_patterns = yaml.safe_load(stream)

    curr_chart_pattern = chart_patterns[desired_chart_pattern]


    scraper = cloudscraper.create_scraper()
    response = scraper.get(finviz_url + curr_chart_pattern)
    html = response.content
    soup = BeautifulSoup(html, "html.parser")
    with open("finviz.html", "w") as f:
        f.write(str(soup.getText))

    ticker_elements = soup.find_all("span")
    ticker_elements = [str(element).split('&lt;b&gt;')[1].split(';')[0] for element in ticker_elements if element.text == " "]
    ticker_elements = [element.strip()[:-3] for element in ticker_elements]

    import requests

    with open('secrets.yml', 'r') as stream:
        json_data = yaml.safe_load(stream)

    base_url = "https://www.alphavantage.co/query?"
    alpha_vantage_api_key = json_data['vantage_api_key']

    def convert_company_name_to_ticker(company_name):
        try:
            params = {
              'function': "SYMBOL_SEARCH",
              'keywords': company_name,
              'apikey': alpha_vantage_api_key
            }

            response = requests.get(base_url, params=params)

            # Get the ticker symbol from the response
            data = response.json()
            ticker_symbol = data['bestMatches'][0]['1. symbol']
            return ticker_symbol
        except Exception as e:
            print("Unable to find the company ticker in alpha vantage api")
            print('==========')
            return None

    company_tickers = []
    import time

    for element in ticker_elements:
        time.sleep(13)
        ticker = convert_company_name_to_ticker(element)
        if ticker:
            company_tickers.append(ticker)

    return company_tickers

get_tickers("Bullish Engulfing")

