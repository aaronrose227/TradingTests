import yfinance as yf

#Make a DataFrame with yfiannce data

df = yf.download("SPY")
print(df.head())

