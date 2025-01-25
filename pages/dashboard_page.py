from dash import html
from dash_spa import register_page

from .common import topNavBar, footer, sideBar, breadCrumbs, banner
from .bootstrap_tables import table1 as teams_table, table2 as leagues_table

register_page(__name__, path="/pages/bets", title="Bets")

layout = html.Main([
        sideBar(),
        topNavBar(),
        html.Div([
            breadCrumbs(["Bets"]),
            banner("League of Legends Bets", "Analysis center of League of Legends teams and tournaments", 'https://betboom.bet.br/')
        ], className='py-4'),
        html.Div([
            html.Div([
                leagues_table(), 
            ], className='col-md-6'), 
            html.Div([
                teams_table(),
            ], className='col-md-6')  # 6 columns on medium screens and up
        ], className='row py-4'),
        footer()
    ], className='content')

