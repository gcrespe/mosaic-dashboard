from dash import html, dcc
from dash_spa import register_page
from .icons import ICON

register_page(__name__, path="/pages/500", title="500", container='full_page')

layout = html.Div([
    html.Main([
        html.Section([
            html.Div([
                html.Div([
                    html.Div([
                        html.H1([
                            "Something has gone",
                            html.Span(" seriously ", className='text-primary'),
                            "wrong"
                        ], className='mt-5'),
                        html.P("It's always time for a coffee break. We should be back by the time you finish your coffee.", className='lead my-4'),
                        dcc.Link([ICON.ARROW_NARROW_LEFT, "Back to homepage"
                        ], href='dashboard', className='btn btn-gray-800 d-inline-flex align-items-center justify-content-center mb-4')
                    ], className='col-12 col-lg-5 order-2 order-lg-1 text-center text-lg-left'),
                    html.Div([
                        html.Img(src='/assets/img/illustrations/500.svg')
                    ], className='col-12 col-lg-7 order-1 order-lg-2 text-center d-flex align-items-center justify-content-center')
                ], className='row align-items-center')
            ], className='container')
        ], className='vh-100 d-flex align-items-center justify-content-center')
    ])
])
