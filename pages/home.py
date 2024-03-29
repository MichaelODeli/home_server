from dash import (
    dcc,
    html,
    Input,
    Output,
    callback,
    register_page,
    State,
    Input,
    Output,
    no_update,
)
import dash_mantine_components as dmc
from flask import request
from datetime import datetime
from controllers import bl_homepage as bl_h
from controllers import cont_homepage
from controllers import service_controller as service

register_page(__name__, path="/", icon="fa-solid:home")
qbittorrent_url = 'http://192.168.3.33:8124'

def layout():
    global qbittorrent_url
    lay = dmc.Container(
        children=[
            dmc.Grid([
                # dmc.Col(span='auto'),
                dmc.Col([bl_h.widget_disk_size()], span='content', className='mobile-widget', id='t'),
                dmc.Col([bl_h.widget_weather()], span='content', className='mobile-widget', id='widget-weather'),
                dmc.Col([bl_h.widget_torrents(qbittorrent_url)], span='content', className='mobile-widget', id='widget_torrents'),
                # dmc.Col(span='auto')
            ],
            align='stretch',
            justify="center",
            className='adaptive-grid')
        ],
        pt=20,
        # style={"paddingTop": 20},
        className='dmc-container adaptive-container'
    )

    # print(f'{request.remote_addr} - - [{now}] | homepage {request.base_url}')
    service.log_printer(request.remote_addr, 'homepage', 'page opened')
    return lay


@callback(
    [
        Output("home-torrents-active", "children"),
        Output("home-torrents-download", "children"),
        Output("home-torrents-upload", "children"),
    ],
    [Input("t", "children")],
)
def toggle_navbar_collapse(_):
    global qbittorrent_url
    return cont_homepage.get_torrent_status(qbittorrent_url)