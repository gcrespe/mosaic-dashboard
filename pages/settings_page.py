from dash import html
from dash_spa import register_page

from .common import topNavBar, footer, buttonBar, sideBar
from .settings import userPhotoCard, profilePhotoCard, coverPhotoCard, generalInformationForm, alertsNotifications, reportsDropdown, newButton, calenderButton


register_page(__name__, path="/pages/settings", title="Settings")

layout = html.Main([
        sideBar(),
        topNavBar(),
        buttonBar(
            lhs=newButton(),
            rhs = [
                calenderButton(),
                reportsDropdown()
            ]
        ),
        html.Div([
            html.Div([
                generalInformationForm(),
                alertsNotifications()
            ], className='col-12 col-xl-8'),
            html.Div([
                html.Div([
                    userPhotoCard(),
                    profilePhotoCard(),
                    coverPhotoCard(),
                ], className='row')
            ], className='col-12 col-xl-4')
        ], className='row'),
        footer()
    ], className='content')

