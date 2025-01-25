from dash import html
from dash_spa import register_page

from .common import breadCrumbs, banner, topNavBar, footer, sideBar
from .bootstrap_tables import table1, table2


register_page(__name__, path="/pages/tables/bootstrap-tables", title="Bootstrap Tables")

layout = html.Main([
        sideBar(),        
        topNavBar(),
        html.Div([
            breadCrumbs(["Tables","Bootstrap tables"]),
            banner("Bootstrap tables", "Dozens of reusable components built to provide buttons, alerts, popovers, and more.", 'https://themesberg.com/docs/volt-bootstrap-5-dashboard/components/tables/')
        ], className='py-4'),
        table1(),
        table2(),
        footer()
    ], className='content')

