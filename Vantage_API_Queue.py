import threading
import queue
import time
import requests
import yaml

"""
    # This is the vantage API queue. This allows me to add API calls that I want to make to the queue and let it be
    executed asynchronously. The advantage of this is that I get rate limited alot less because I have 7 keys - each
    binded to one of my gmail accounts which I cycle between. To achieve the same, add to your vantage_api_key.yaml
    the api keys you have.
    
    e.g vantage_api_key_1: INSERT_YOUR_FIRST_API_KEY_HERE
        vantage_api_key_2: INSERT_YOUR_SECOND_API_KEY_HERE
"""
class Test:
    def __init__(self):
        self.queue = queue.Queue()
        with open('vantage_api_key.yaml', 'r') as f:
            api_keys = yaml.safe_load(f)
        self.keys = [value for key, value in api_keys.items()]
        for keys in self.keys:
            self.queue.put(keys)

    def get_key(self):
        return self.queue.get()

    def add_key_back_to_queue(self, key):
        def run():
            time.sleep(12)
            self.queue.put(key)

        threading.Thread(target=run).start()

    def execute(self, function, base_url, params, headers=None):
        while self.queue.empty():
            time.sleep(1)
        key = self.get_key()
        params['apikey'] = key

        if headers:
            response = function(base_url, params, headers)
        else:
            response = function(base_url, params)

        print("response: ", response)
        threading.Thread(self.add_key_back_to_queue(key)).start()
        return response

test = Test()
base_url = "https://www.alphavantage.co/query?"
params = {
    'function': "SYMBOL_SEARCH",
    'keywords': "Apple Inc",
}

for i in range(12):
    test.execute(lambda x, y: requests.get(x, y), base_url, params)

