from dash import html, dcc
from dash_spa import register_page
from ..common import breadCrumbs, banner, topNavBar, footer, sideBar

from ..icons import ICON, FACEBOOK, TWITTER, GITHUB
from .modals import default, notification, sign_in, sign_out, achievement, subscribe

register_page(__name__, path="/pages/components/modals", title="Modals")


def modals():
    return html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        default(),
                        notification(),
                        sign_in(),
                        sign_out(),
                        achievement(),
                        subscribe()
                    ], className='row d-block mt-4')
                ], className='card-body')
            ], className='card border-0 shadow')
        ], className='col-12 mb-4')
    ], className='row')

layout = html.Main([
        sideBar(),        
        topNavBar(),
        html.Div([
            breadCrumbs(["Components", "Modals"]),
            banner("Modals", "Dozens of reusable components built to provide buttons, alerts, popovers, and more.", 'https://themesberg.com/docs/volt-bootstrap-5-dashboard/components/modals/')
        ], className='py-4'),
        modals(),
        footer()
    ], className='content')
