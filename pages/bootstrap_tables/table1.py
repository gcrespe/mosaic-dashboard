from collections import OrderedDict
import pandas as pd
from dash import html
from dash_spa.components import TableContext
from .basic_table import BasicTable

data = OrderedDict([
    ('#',['1', '2', '3', '4', '5', '6', '7']),
    ('Traffic Source',['Direct', 'Google Search', 'youtube.com', 'yahoo.com', 'twitter.com', 'asdas', 'asdasd']),
    ('Source Type',['Direct', 'Search/Organic', 'Social', 'Referral', 'Social', 'asdaasd', 'asdas']),
    ('Category',['-', '-', 'Arts and Entertainment', 'News and Media', 'Social Networks', 'adsasd', '123123']),
    ('Global Rank',['--', '--', '#2', '#11', '#4', '#1', '6%']),
    ('Traffic Share',['51%', '18%', '18%', '8%', '4%', '6%', '19%']),
    ('Change',['2.45%', '17.78%', '-', '-9.45%', '-', '-', '-']),
    ])


df = pd.DataFrame.from_dict(data)

def progressBar(value):
    value = value[0:-1]
    return html.Td([
        html.Div([
            html.Div([
                html.Div(value, className='small fw-bold')
            ], className='col-12 col-xl-2 px-0'),
            html.Div([
                html.Div([
                    html.Div(className='progress-bar bg-dark',
                             role='progressbar',
                             style={"width": f"{value}%"})
                ], className='progress progress-lg mb-0')
            ], className='col-12 col-xl-10 px-0 px-xl-1')
        ], className='row d-flex align-items-center')
    ])


class TrafficTable(BasicTable):

    def tableRow(self, index, args):

        cid, ts, st, cat, rank, share, change = args.values()

        return html.Tr([
            html.Td([
                html.A(cid, href='#', className='text-primary fw-bold')
            ]),
            html.Td([
                ts
            ], className='fw-bold d-flex align-items-center'),
            html.Td(st),
            html.Td(cat),
            html.Td(rank),
            progressBar(share),
            self.numberAndArrow(change)
        ])

@TableContext.Provider(id='bootstrap_table1')
def table1():

    table = TrafficTable(
        data=df.to_dict('records'),
        columns=[{'id': c, 'name': c} for c in df.columns])


    return html.Div([
        html.Div([
            html.Div(table, className='table-responsive')
        ], className='card-body')
    ], className='card border-0 shadow mb-4', style={'maxHeight': '40vh', 'overflowY': 'auto'})
