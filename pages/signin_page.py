from dash import html, dcc
from dash_spa import register_page
from .common import background_img
from .icons import ICON, FACEBOOK, TWITTER, GITHUB

register_page(__name__, path="/", title="Sign in", container='full_page')

layout = html.Div([
    # NOTICE: You can use the _analytics.html partial to include production code specific code & trackers
    html.Main([
        # Section
        html.Section([
            html.Div([
                html.Div([
                    html.Div([
                        html.Div([
                            html.Div([
                                html.H1("Sign in", className='mb-0 h3')
                            ], className='text-center text-md-center mb-4 mt-md-0'),
                            html.Form([
                                # Form
                                html.Div([
                                    html.Label("Your Email", htmlFor='email'),
                                    html.Div([
                                        html.Span(ICON.MAIL, className='input-group-text', id='basic-addon1'),
                                        dcc.Input(type='email', className='form-control', placeholder='example@company.com', id='email', required='')
                                    ], className='input-group')
                                ], className='form-group mb-4'),
                                # End of Form
                                html.Div([
                                    # Form
                                    html.Div([
                                        html.Label("Your Password", htmlFor='password'),
                                        html.Div([
                                            html.Span(ICON.LOCK_CLOSED, className='input-group-text', id='basic-addon2'),
                                            dcc.Input(type='password', placeholder='Password', className='form-control', id='password', required='')
                                        ], className='input-group')
                                    ], className='form-group mb-4'),
                                    # End of Form
                                    html.Div([
                                        html.Div([
                                            dcc.Input(className='form-check-input', type='checkbox', value='', id='remember'),
                                            html.Label("Remember me", className='form-check-label mb-0', htmlFor='remember')
                                        ], className='form-check'),
                                        html.Div([
                                            dcc.Link("Lost password?", href='./forgot-password', className='small text-right')
                                        ])
                                    ], className='d-flex justify-content-between align-items-top mb-4')
                                ], className='form-group'),
                                dcc.Link([
                                    html.Div([
                                        html.Button("Sign in", type='submit', className='btn btn-gray-800')
                                    ], className='d-grid')
                                ], href='/pages/dashboard')
                            ], action='#', className='mt-4'),
                            html.Div([
                                html.Span([
                                    "Not registered? ",
                                    dcc.Link("Create account", href='./sign-up', className='fw-bold')
                                ], className='fw-normal')
                            ], className='d-flex justify-content-center align-items-center mt-4')
                        ], className='bg-white shadow border-0 rounded border-light p-4 p-lg-5 w-100 fmxw-500')
                    ], className='col-12 d-flex align-items-center justify-content-center')
                ], className='row justify-content-center form-bg-image', style=background_img("/assets/img/illustrations/signin.svg"))
            ], className='container')
        ], className='vh-lg-100 mt-5 mt-lg-0 bg-soft d-flex align-items-center')
    ])
])
