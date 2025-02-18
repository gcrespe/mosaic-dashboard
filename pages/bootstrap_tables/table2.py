from collections import OrderedDict
import pandas as pd
from dash import html
from dash_spa.components import TableContext
from .basic_table import BasicTable

data = OrderedDict([

    ('Country',['United States', 'Canada', 'United Kingdom', 'France', 'Japan', 'Germany', 'United States', 'Canada', 'United Kingdom', 'France']),
    ('All',['106', '76', '147', '112', '115', '220', '106', '76', '147', '112']),
    ('All Change',['-5', '17', '10', '3', '-12', '-56', '-5', '17', '10', '3']),
    ('Travel & Local',['3', '4', '5', '5', '6', '7', '3', '4', '5', '5']),
    ('Travel & Local Change',['=', '=', '=', '1', '-1', '-3', '=', '=', '=', '1']),
    ('Widgets',['32', '30', '34', '34', '37', '30', '32', '30', '34', '34']),
    ('Widgets Change',['3', '3', '7', '-2', '-5', '2', '3', '3', '7', '-2']),
    ])

FLAGS = {
    "United States": '../../assets/img/flags/united-states-of-america.svg',
    "Canada": '../../assets/img/flags/canada.svg',
    "United Kingdom": '../../assets/img/flags/united-kingdom.svg',
    "France": '../../assets/img/flags/france.svg',
    "Japan": '../../assets/img/flags/japan.svg',
    "Germany": '../../assets/img/flags/germany.svg',
}


df = pd.DataFrame.from_dict(data)

class TravelTable(BasicTable):

    def tableRow(self, index, args):

        country, all, change, tal, talCh, widgets, widgetsCh = args.values()

        return  html.Tr([
            html.Td([
                html.A([
                    html.Div([
                        html.Span(country, className='h6')
                    ])
                ], href='#', className='d-flex align-items-center')
            ], className='border-0'),
            html.Td(all, className='border-0 fw-bold'),
            self.numberAndArrow(change),
            html.Td(tal, className='border-0 fw-bold'),
            self.numberAndArrow(talCh),
            html.Td(widgets, className='border-0'),
            self.numberAndArrow(widgetsCh),

        ])

@TableContext.Provider(id='bootstrap_table2')
def table2():

    table = TravelTable(
        data=df.to_dict('records'),
        columns=[{'id': c, 'name': c} for c in df.columns])

    return html.Div([
        html.Div([
            html.Div(table, className='table-responsive')
        ], className='card-body')
    ], className='card border-0 shadow', style={'maxHeight': '40vh', 'overflowY': 'auto'})
