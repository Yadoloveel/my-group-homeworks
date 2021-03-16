import dash_html_components as html
import dash_bootstrap_components as dbc
from datetime import date

from callbacks import *


"""
layout - of the app and it describes what the appcovd.py looks like
 1. main_page with graphs (all_covid_map, all_covid_barh, treemap)
 2. pgstat_layout with graph (country_subplt) - included 7 subgraphs
 3. pghronolog_layout with graphs (sunburst, map_covid_date) 
"""

main_page = html.Div([

    dbc.Row([
        dbc.Col(dcc.Markdown(f'## Global situation, at **{date_head()}**, '
                             f' regarding coronavirus.'),
                className='text-center text-info mr-1',
                width=12)
    ], ),

    dbc.Row([
        dbc.Col(html.H4(allsumhead()),
                className='text-center text-primary mr-1',
                width=12)
    ], ),

    dbc.ButtonGroup([
        dbc.DropdownMenu([
            dbc.DropdownMenuItem(dcc.Link('Statistics', href='/pgstat')),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem(dcc.Link('Chronology', href='/pghronolog'))
            ],
            label="Select",
            color='info',
            className="mr-1",
            group=True),
        dbc.Button(id="btn_cases",
                   n_clicks_timestamp=1,
                   children='Cases',
                   color="primary",
                   className="mr-1"),
        dbc.Button(id="btn_deaths",
                   n_clicks_timestamp=0,
                   children='Deaths',
                   color="danger",
                   className="mr-1"),
        dbc.Button("Update_data",
                   id="update",
                   n_clicks=0,
                   color='info',
                   outline=True,
                   className="mr-1")
        ], className='mb-3'),

    dcc.Graph(id='all_covid_map', figure={}, style={'width': '100%',
                                                    'height': '500px'}),

    dcc.Graph(id='all_covid_barh', figure={}, style={'width': '100%',
                                                     'height': '350px'}),

    dcc.Graph(id='treemap', figure={}, style={'width': '100%',
                                              'height': '700px'})
]),

pgstat_layout = html.Div([
    dbc.Row([
        dbc.Col(html.H4(allsumhead()),
                className='text-center text-info mr-1',
                width=12)
    ], ),

    dbc.ButtonGroup([
        dbc.DropdownMenu([
            dbc.DropdownMenuItem(dcc.Link('Chronology', href='/pghronolog')),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem(dcc.Link('To the main', href='/'))
        ],
            label="Select",
            color='info',
            className="mr-1",
            group=True),
    ], className='mb-3'),
    html.H4(html.B('Сhoice country to report:'),
            className='text-left text-link mr-1'),
    dcc.Dropdown(id="dd_country",
                 clearable=False,
                 value="Ukraine",
                 options=[{"label": i, "value": i}
                          for i in groupmax()['Country']],
                 className='text-center text-link mr-2',
                 # style={'height': '40px'}
                 ),

    dcc.Graph(id='country_subplt', figure={}, style={'width': '100%',
                                                     'height': '1400px'})
]),

pghronolog_layout = html.Div([

    dbc.Row([
        dbc.Col(html.H4(allsumhead()),
                className='text-center text-info mr-1',
                width=12)
    ], ),

    dbc.ButtonGroup([
        dbc.DropdownMenu([
            dbc.DropdownMenuItem(dcc.Link('Statistics', href='/pgstat')),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem(dcc.Link('To the main', href='/'))
        ],
            label="Select",
            color='info',
            className="mr-1",
            group=True),
        html.Br(),
        dbc.Button(id="btn_cases",
                   n_clicks_timestamp=1,
                   children='Cases',
                   color="primary",
                   className="mr-1"),
        dbc.Button(id="btn_deaths",
                   n_clicks_timestamp=0,
                   children='Deaths',
                   color="danger",
                   className="mr-1"),
        html.Tr(className='mr-3'),
        html.H4(html.B('Сhoice Date reported:'),
                className='text-left text-link mr-1'),
        dcc.DatePickerRange(id='date_picker',
                            min_date_allowed=date(2020, 1, 3),
                            display_format='Y-MM-DD',
                            # clearable=True,
                            start_date='2020-01-03',
                            end_date='2020-01-04',
                            with_portal=True
                            )
    ], className='mb-3'),
    html.H4('Chronology of the epidemic by continents:'),
    html.Br(),
    dcc.Graph(id="sunburst", style={'width': '100%',
                                    'height': '700px'}),
    html.Br(),
    html.H5(f"Chronology of the world epidemic by date: "),
    dcc.Graph(id='map_covid_date', figure={}, style={'width': '100%',
                                                     'height': '700px'})

])
