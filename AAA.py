
import pandas as pd
import ssl
import urllib3

ssl._create_default_https_context = ssl._create_unverified_context
calls_df, = pd.read_html("https://cn.tradingview.com/markets/currencies/rates-major/", header=0)

print(calls_df.to_json(orient="records", date_format="iso"))
calls_df.to_csv("calls.csv", encoding='utf_8_sig', index=False)