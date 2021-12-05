from yahoo_fin.stock_info import get_data, get_analysts_info, tickers_sp500, get_company_info
import pandas as pd

pd.set_option('display.max_rows', 6000)
pd.set_option('display.max_columns', 6000)


# putem da start date si end date ca argument la functie daca vrem sa folosim pentru un grafic
def _get_data(ticker, _start_date="12/01/2014", _end_date="12/02/2021", _interval = '1d'):
    daily = get_data(ticker, start_date=_start_date, end_date=_end_date, index_as_date=False, interval = _interval)
    daily.drop(["ticker", "adjclose"], axis=1, inplace=True)
    return daily.values.tolist()


def _analyst_data(ticker):
    info = get_analysts_info(ticker)
    info.pop('Earnings Estimate')
    info.pop('Earnings History')
    info.pop('EPS Revisions')
    info.pop('Growth Estimates')
    info.pop('EPS Trend')

    rawData = str(info['Revenue Estimate']).split()

    _usableData = []
    _usableData.append(rawData[20])
    _usableData.append(rawData[21])
    _usableData.append(rawData[42])
    _usableData.append(rawData[43])
    _usableData.append(rawData[54])
    _usableData.append(rawData[55])
    _usableData.append(rawData[66])
    _usableData.append(rawData[67])
    return _usableData

#  index_as_date=True
# '1d', '1wk', '1mo', or '1m'
# open        high         low       close     volume ordinea elementelor din lista