import sys
import dash_bootstrap_components as dbc
from local_functions import get_data
from dash import Dash, html, dcc,Input, Output, State, callback
currencies = ['AFN','ALL','DZD','USD','EUR','AOA','XCD','XCD','ARS','AMD','AWG','AUD','EUR','AZN','BSD','BHD','BDT','BBD','BYN','EUR','BZD','XOF','BMD','BTN','INR','BOB','BOV','USD','BAM','BWP','NOK','BRL','USD','BND','BGN','XOF','BIF','CVE','KHR','XAF','CAD','KYD','XAF','XAF','CLF','CLP','CNY','AUD','AUD','COP','COU','KMF','CDF','XAF','NZD','CRC','EUR','CUC','CUP','ANG','EUR','CZK','XOF','DKK','DJF','XCD','DOP','USD','EGP','SVC','USD','XAF','ERN','EUR','ETB','EUR','FKP','DKK','FJD','EUR','EUR','EUR','XPF','EUR','XAF','GMD','GEL','EUR','GHS','GIP','EUR','DKK','XCD','EUR','USD','GTQ','GBP','GNF','XOF','GYD','HTG','USD','AUD','EUR','HNL','HKD','HUF','ISK','INR','IDR','XDR','IRR','IQD','EUR','GBP','ILS','EUR','JMD','JPY','GBP','JOD','KZT','KES','AUD','KPW','KRW','KWD','KGS','LAK','EUR','LBP','LSL','ZAR','LRD','LYD','CHF','EUR','EUR','MOP','MGA','MWK','MYR','MVR','XOF','EUR','USD','EUR','MRU','MUR','EUR','XUA','MXN','MXV','USD','MDL','EUR','MNT','EUR','XCD','MAD','MZN','MMK','NAD','ZAR','AUD','NPR','EUR','XPF','NZD','NIO','XOF','NGN','NZD','AUD','USD','NOK','OMR','PKR','USD','PAB','USD','PGK','PYG','PEN','PHP','NZD','PLN','EUR','USD','QAR','MKD','RON','RUB','RWF','EUR','EUR','SHP','XCD','XCD','EUR','EUR','XCD','WST','EUR','STN','SAR','XOF','RSD','SCR','SLE','SGD','ANG','XSU','EUR','EUR','SBD','SOS','ZAR','SSP','EUR','LKR','SDG','SRD','NOK','SZL','SEK','CHE','CHF','CHW','SYP','TWD','TJS','TZS','THB','USD','XOF','NZD','TOP','TTD','TND','TRY','TMT','USD','AUD','UGX','UAH','AED','GBP','USD','USD','USN','UYI','UYU','UZS','VUV','VEF','VED','VND','USD','USD','XPF','MAD','YER','ZMW','ZWL','EUR']
ALLOWED_TYPES = ("number")
app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    html.H1("Currency Converter", style={'text-align': 'center'}),
    html.Hr(),
    html.Br(),
    dbc.Row(
        [
        dbc.Col(dcc.Input(id="amt_currency",type="number",placeholder="Amount for conversion",style={'width':'100%'})),
        ]
    ),
    html.Br(),
    dbc.Row([
            dbc.Col(dcc.Dropdown(currencies, '', id='home-currency',placeholder="Select your home currency"),lg=6, sm=12),
            dbc.Col(dcc.Dropdown(currencies, '', id='convert-currency',placeholder="Select the currency you want to convert too"),lg=6, sm=12),
        ]),
    html.Br(),
    dbc.Row([
                dbc.Col(html.Button(id='submit-button-state', n_clicks=0, children='Submit',style={'width':'100%'}),),
            ]),
    html.Div(children='',id='exchange-rate')
])

@callback(Output(component_id='exchange-rate', component_property='children'),
    Input(component_id='submit-button-state', component_property='n_clicks'),
    State(component_id='amt_currency', component_property='value'),
    State(component_id='home-currency', component_property='value'),
    State(component_id='convert-currency', component_property='value'),
)
def update_output_div(n_clicks,amnt,home,convert):
    if n_clicks > 0:
        return get_data(home,amnt,convert)
    else:
        return "Please press submit"


if __name__ == '__main__':
    #print(sys.executable)
    app.run(debug=True)


    # base_currency = input('Please enter the currency you have (e.g. GBP): ').upper()
    # try:
    #     amt_currency = float(input('Please enter the amount of the currency you have (number only): '))
    # except Exception as e:
    #     print(e)
    #     sys.exit(1)
    # src_currency = input('Please enter the currency you want to compare too (e.g. USD): ').upper()
    # if base_currency in currencies:
    #     if src_currency in currencies:
    #         get_data(base_currency,amt_currency, src_currency)
    # else:
    #     print('Please make sure you have entered a valid currency')

