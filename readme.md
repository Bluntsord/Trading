## QuickStart:

This is a python project that will help me make buttloads of money thank you.

main.py: Runs and pulls data from vantage. Also works with the tiger brokers api and is synced to my tiger brokers
account using the private key. If you want to do the same, you will need a tiger brokers account and
get your own private key for it

extract_tickers.py: Extracts tickers from the finviz and saves them to a file

### Idea:

To get a decent engine there are some questions we must address:

**How to choose what stock to buy?**
<br>
1: [Extract the appropriate tickers from finviz](ExtractTickers.py). This way they handle the charting instead of me.
2: Run some machine learning or according to the 
statistics provided from [success_rates](https://the5ers.com/price-pattern-study/)

**How to filter and validate the stocks to buy?**
<br>
1: Do some sentiment analysis on the stock. This way we can see if the stock is being talked about
2: Do some technical analysis on the stock. This way we can know how reliable the above data from finviz is

**When to buy the specified stock?**
<br>
1: Use moving average breakout strategy
2: Use fibonacci retracement strategy

**When to exit the position of the stock?**
<br>
1: Some fundamental analysis of the stock
2: Technical analysis of the stock
3: Market conditions of the stock
4: Risk tolerance

Final Step: Profit

# Remember!!!

![dunning_kruger](./Assets/DunningKrugerEffect.jpg)