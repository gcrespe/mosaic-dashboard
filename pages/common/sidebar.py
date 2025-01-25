from dash import html, dcc
from dash_spa import prefix
from dash_spa.components.dropdown_folder_aoi import DropdownFolderContext, DropdownFolderAIO, SidebarNavItem, dropdownFolderEntry

from ..icons.hero import ICON
from .mobile_nav import mobileSidebarHeader


def _sidebarLink(text, icon, href, hyperlink=False, target=""):
    Element = html.A if hyperlink else dcc.Link
    el = Element([
            html.Div([
                html.Span([
                    icon
                ], className='sidebar-icon'),
                html.Span(text, className='mt-1 ms-1 sidebar-text')
            ], className="align-items-center justify-content-center")
        ], href=href, className='nav-link mb-3')

    if target:
        el.target = target

    return SidebarNavItem(el, SidebarNavItem.is_active(href))


def _sidebarButtonLink(text, icon, href):
    return SidebarNavItem([
        dcc.Link([
            html.Span([
                icon
            ], className='sidebar-icon d-inline-flex align-items-center justify-content-center'),
            html.Span(text, className="sidebar-text")
        ], href=href, className='btn btn-secondary d-flex align-items-center justify-content-center btn-upgrade-pro')
    ], active=SidebarNavItem.is_active(href))

def _sidebarLogo(icon, href):
    return SidebarNavItem([
        dcc.Link([
            html.Span([
                icon
            ], className='sidebar-icon d-inline-flex align-items-center justify-content-center'),
            html.Span(className="sidebar-text")
        ], href=href, className='btn text-secondary me-3 d-flex align-items-center justify-content-center mb-3 pt-md-4')
    ], active=SidebarNavItem.is_active(href))



@DropdownFolderContext.Provider()
def sideBar():
    pid = prefix('sidebar')
    return html.Nav([
        html.Div([

            mobileSidebarHeader(),

            # Sidebar List of entries

            html.Ul([

                # Logo
                _sidebarLogo(ICON.MOSAIC, '../pages/upgrade-to-pro'),
                
                _sidebarLink("Bets", ICON.BETS, '/pages/bets'),
                _sidebarLink("Transactions", ICON.CREDIT_CARD, '/pages/transactions'),
                _sidebarLink("Settings", ICON.VIEW_GRID, '/pages/settings'),
                _sidebarLink("Calendar", ICON.CALENDER, 'https://demo.themesberg.com/volt-pro/pages/calendar'),

                DropdownFolderAIO([
                    dropdownFolderEntry("Bootstrap Tables", '/pages/tables/bootstrap-tables'),
                ], "Tables", ICON.TABLE, id=pid('tables')),

                # Page examples drop down

                DropdownFolderAIO([
                    dropdownFolderEntry("Sign In", '/pages/sign-in'),
                    dropdownFolderEntry("Sign Up", '/pages/sign-up'),
                    dropdownFolderEntry("Forgot password", '/pages/forgot-password'),
                    dropdownFolderEntry("Reset password", '/pages/reset-password'),
                    dropdownFolderEntry("Lock", '/pages/lock'),
                    dropdownFolderEntry("404 Not Found", '/pages/???'),
                    dropdownFolderEntry("500 Not Found", '/pages/500'),
                ], "Page examples", ICON.PAGES, id=pid('examples')),

                # Components  drop down

                DropdownFolderAIO([
                    dropdownFolderEntry("Buttons", '/pages/components/buttons'),
                    dropdownFolderEntry("Notifications", '/pages/components/notifications'),
                    dropdownFolderEntry("Forms", '/pages/components/forms'),
                    dropdownFolderEntry("Modals", '/pages/components/modals'),
                    dropdownFolderEntry("Typography", '/pages/components/typography'),
                ], "Components", ICON.ARCHIVE, id=pid('components')),

            ], className='nav flex-column')
        ], className='sidebar-inner px-4')
    ], id='sidebarMenu', className='sidebar d-lg-block bg-gray-800 text-white collapse')
