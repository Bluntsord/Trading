from tigeropen.common.consts import (Language,        # Language
                                Market,           # Market
                                BarPeriod,        # Size of each time window of the K-Line
                                QuoteRight)       # Price adjustment type
from tigeropen.tiger_open_config import TigerOpenClientConfig
from tigeropen.common.util.signature_utils import read_private_key
from tigeropen.quote.quote_client import QuoteClient

import requests
import yaml
import json
from alpha_vantage.timeseries import TimeSeries

# Almost all requests related to pulling market quote data use the methods of QuoteClient,
# first generate the client config which used to initialize QuoteClient. The config contain developer's information like tiger_id, private_key, account

with open('secrets.yml', 'r') as stream:
    json_data = yaml.safe_load(stream)

def get_client_config(sandbox=False):
    """
    https://quant.itigerup.com/#developer   query developer infos
    """
    client_config = TigerOpenClientConfig(sandbox_debug=sandbox)
    client_config.private_key = read_private_key('./private_key.pem')
    client_config.tiger_id = json_data['tiger_id']
    client_config.account = json_data['tiger_paper_account_id']
    # client_config.language = Language.zh_CN  # optional, default en_US
    # client_config.timezone = 'US/Eastern' # default timezone
    return client_config

# initialize ClientConfig
client_config = get_client_config()

vantage_api_key = json_data['vantage_api_key']
ts = TimeSeries(key=vantage_api_key, output_format='pandas', indexing_type='date')

data, meta_data = ts.get_intraday(symbol='AAPL', interval='5min', outputsize='full')
print(data.head(2))



