import queue as q
import yaml
import requests
import time
import asyncio

with open('vantage_api_key.yaml', 'r') as f:
    api_keys = yaml.safe_load(f)

keys = [value for key, value in api_keys.items()]

class Vantage_API_queue:
    def __init__(self):
        self.queue = q.Queue()
        for key in keys:
            self.queue.put(key)
        self.available_keys = keys

    async def execute(self, baseurl, params):
        curr_key = self.queue.get(timeout=12.1)
        params["apikey"] = curr_key
        response = requests.get(baseurl, params=params)
        self.lock(curr_key)
        if response.status_code == 200:
            return response
        print("Error: ", response.status_code)
        return None


    async def lock(self, key):
        self.available_keys.remove(key)
        # This is based on the rate limiter
        time.sleep(12.1)


    def release(self, key):
        self.available_keys.append(key)
        self.queue.put(key)


base_url = "https://www.alphavantage.co/query?"
params = {
    'function': "SYMBOL_SEARCH",
    'keywords': "Apple Inc",
}
vantage_queue = Vantage_API_queue()
response = vantage_queue.execute(base_url, params)
data = response.json()
ticker_symbol = data['bestMatches'][0]['1. symbol']
print(ticker_symbol)