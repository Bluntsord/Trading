import re

import yaml
from bs4 import BeautifulSoup
import cloudscraper

finviz_url = "https://finviz.com/screener.ashx?v=210&s="
with open("finviz_chart_patterns.yaml", "r") as stream:
    chart_patterns = yaml.safe_load(stream)

chart_pattern = chart_patterns['channel_up']


scraper = cloudscraper.create_scraper()
response = scraper.get(finviz_url + chart_pattern)
html = response.content
soup = BeautifulSoup(html, "html.parser")
ticker_elements = soup.find_all("span")
ticker_elements = [str(element).split('&lt;b&gt;')[1].split(';')[0] for element in ticker_elements if element.text == " "]
ticker_elements = [element.strip()[:-3] for element in ticker_elements]
print(ticker_elements)

