import analysis as ans
import json
from email import utils
import datetime
ans.tickers_sp500

def getAllTickers():
    return json.dumps(ans.tickers_sp500())

def getDataForTicker(ticker, start_date, end_date, interval):
    data_list = ans._get_data(ticker, _start_date=start_date, _end_date = end_date, _interval = interval)
    data_dict = [{"x":int(round(l[0].timestamp() * 1000)),"o":l[1],"h":l[2],"l":l[3],"c":l[4],"v":l[5]} for l in data_list]
    return json.dumps(data_dict)

def getAnalystData(ticker):
    return json.dumps(ans._analyst_data(ticker))
# print(searchTickers())
def companyInfo(ticker):
    return str(ans.get_company_info(ticker))