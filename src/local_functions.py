from keys import *
import requests
import json
import pandas as pd

def get_data(baseCurr, amnt, curr='USD'): #want to move this into its own folder
    url1 = url + access_key + '/latest/'+baseCurr
    r = requests.get(url1)
    if r.status_code == 200:
        data = json.loads(r.text)
        pd.set_option('display.max_columns', None)
        df = pd.DataFrame.from_dict(data)


        base_conv = df.loc[[curr],['conversion_rates']]
        base_conv2 = base_conv.iloc[0,0]
        base_conv2 = float(base_conv2)

        calc = amnt * base_conv2
        calc = round(calc,2)

        return 'You have ' + str(amnt) + baseCurr + ' which converts to ' + str(calc) + curr + ' with an exchange rate of ' + str(base_conv2)
    else:
        print(r.status_code)