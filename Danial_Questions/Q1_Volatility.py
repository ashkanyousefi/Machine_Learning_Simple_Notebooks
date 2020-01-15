import pandas as pd
import numpy as np

def get_most_volatile(prices):
    """Return the ticker symbol for the most volatile stock.
    
    Parameters
    ----------
    prices : pandas.DataFrame
        a pandas.DataFrame object with columns: ['ticker', 'date', 'price']
    
    Returns
    -------
    ticker : string
        ticker symbol for the most volatile stock
    """
    # TODO: Fill in this function.
    #I have tried to select the specific column and then apply the standard deviation to 
    # check the volatility to a column to see how it works.
    
    
    price_modified=prices.groupby(prices['ticker'])
    # print(price_modified.price.rolling(2).std())



def test_run(filename='prices.csv'):
    """Test run get_most_volatile() with stock prices from a file."""
    prices = pd.read_csv(filename, parse_dates=['date'])
    print("Most volatile stock: {}".format(get_most_volatile(prices)))
    
    


if __name__ == '__main__':
    test_run()
