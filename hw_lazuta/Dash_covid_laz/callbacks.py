import plotly.express as px
import plotly.graph_objects as go

import pyautogui
from dash.dependencies import Input, Output
from plotly.subplots import make_subplots

from appcovd import app
from df_datacsv import *

# global variable cases & deaths
cases = 'Cumulative_cases'
deaths = 'Cumulative_deaths'


@app.callback(Output("update", "n_clicks"),
              [Input("update", "n_clicks")]
              )
def data_alert(n):
    """
    func for buttom update_data on the main_page
    :param n:
    :return: True or False
    """
    if n:
        try:
            urlcsv()
            allsumhead()
            return pyautogui.alert(title=f"Message!!!",
                                   text=f"Success! Data update at "
                                        f"{date_head()}.",
                                   button='OK')
        except EnvironmentError:
            return not pyautogui.alert(title=f"Message!!!",
                                       text=f"Error! "
                                            f"Data update process error."
                                            f" Try again!",
                                       button='OK')


@app.callback(Output('all_covid_map', 'figure'),
              [Input("btn_cases", "n_clicks_timestamp"),
               Input("btn_deaths", "n_clicks_timestamp")],
              )
def update_map_all(btn_cases, btn_deaths):
    """
    func updated data in graph all_covid_map if btn_cases,btn_deaths on_clicks
    main)
    :param btn_cases:
    :param btn_deaths:
    :return: fig for cases or deaths
    """
    if btn_cases > btn_deaths:
        fig = px.choropleth_mapbox(
            data_frame=groupmax(),
            geojson=counties,
            featureidkey='properties.name',
            locations='Country',
            color=cases,
            color_continuous_scale=px.colors.carto.Bluyl,
            hover_data=['Country', cases],
            mapbox_style="carto-positron",
            zoom=1,
            opacity=0.3,
            title='Cumulative cases in the world:'
        )
        fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
        return fig
    elif btn_deaths > btn_cases:
        fig = px.choropleth_mapbox(
            data_frame=groupmax(),
            geojson=counties,
            featureidkey='properties.name',
            locations='Country',
            color=deaths,
            color_continuous_scale='reds',
            hover_data=['Country', deaths],
            mapbox_style="carto-positron",
            zoom=1,
            opacity=0.3,
            title='Cumulative deaths in the world:'
        )
        fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
        return fig


@app.callback(
    Output("all_covid_barh", "figure"),
    [Input("btn_cases", "n_clicks_timestamp"),
     Input("btn_deaths", "n_clicks_timestamp")])
def update_barh(btn_cases, btn_deaths):
    """
    func update data in graph all_covid_barh if btn_cases,btn_deaths on_clicks
    :param btn_cases:
    :param btn_deaths:
    :return: fig for cases or deaths
    """
    if btn_cases > btn_deaths:
        fig = px.bar(region_main(), x="Date_reported", y=cases,
                     # orientation='h',
                     color='WHO_region',
                     title='Cumulative cases in the regions:')
        return fig
    elif btn_deaths > btn_cases:
        fig = px.bar(region_main(), x="Date_reported", y=deaths,
                     # orientation='h',
                     color='WHO_region',
                     title='Cumulative deaths in the regions:')
        return fig


@app.callback(
    Output("treemap", "figure"),
    [Input("btn_cases", "n_clicks_timestamp"),
     Input("btn_deaths", "n_clicks_timestamp")],
)
def update_treemap(btn_cases, btn_deaths):
    """
    func update data in graph treemap if btn_cases,btn_deaths on_clicks
    :param btn_cases:
    :param btn_deaths:
    :return: figure for cases or deaths
    """
    if btn_cases > btn_deaths:
        figure = px.treemap(region_stat(),
                            path=[px.Constant('world'), 'WHO_region',
                                  'Country'],
                            values=cases,
                            color='Country',
                            color_continuous_scale='RdBu',
                            )
        return figure
    elif btn_deaths > btn_cases:
        figure = px.treemap(region_stat(),
                            path=[px.Constant('world'), 'WHO_region',
                                  'Country'],
                            values=deaths,
                            color='Country', hover_data=['Country'],
                            color_continuous_scale='RdBu',
                            )
        return figure


@app.callback(
    Output("country_subplt", "figure"),
    [Input("dd_country", "value")]
)
def update_subplt(dd_country):
    """
    func update data by country in graphs subplots-graph(Cumulative cases,
    Cumulative deaths, New cases, New deaths, table data
    if btn_cases, btn_deaths on_clicks
    :param dd_country:
    :return: fig for cases or deaths by country in
    """
    if dd_country is not None:
        sub_state = subplt_country(dd_country)
        fig = make_subplots(
            rows=4, cols=2,
            specs=[[{"type": "scatter"}, {"type": "scatter"}],
                   [{"type": "scatter"}, {"type": "scatter"}],
                   [{"type": "domain"}, {"type": "domain"}],
                   [{"type": "table", "colspan": 2}, None]
                   ],
            shared_xaxes=True,
            vertical_spacing=0.04,
            subplot_titles=(f"Cumulative cases - "
                            f"{space_num(max(sub_state[cases]))}",
                            f"Cumulative deaths - "
                            f"{space_num(max(sub_state[deaths]))}",
                            f"New cases - {space_num(topScatter1(sub_state))}",
                            f"New deaths - {space_num(topScatter2(sub_state))}"
                            )
        )
        fig.add_trace(
            go.Scatter(
                x=sub_state["Date_reported"],
                y=sub_state[cases],
                mode="lines",
                name=f"Cumulative_cases "
            ),
            row=1, col=1
        )
        fig.add_trace(
            go.Scatter(
                x=sub_state["Date_reported"],
                y=sub_state[deaths],
                mode="lines",
                name="Cumulative_deaths"
            ),
            row=1, col=2
        )
        fig.add_trace(
            go.Scatter(
                x=sub_state["Date_reported"],
                y=sub_state['New_cases'],
                mode="lines",
                name="New_cases"
            ),
            row=2, col=1
        )
        fig.add_trace(
            go.Scatter(
                x=sub_state["Date_reported"],
                y=sub_state['New_deaths'],
                mode="lines",
                name="New_deaths"
            ),
            row=2, col=2
        )
        fig.add_trace(
            go.Pie(
                labels=['Cases_country', 'Globally_cases'],
                values=[max(sub_state[cases]),
                        groupmax()['Cumulative_cases'].sum()],
                name=cases,
                textinfo='label+percent',
                insidetextorientation='auto',
                pull=[0, 0.1],
                hole=.2
            ), 3, 1
        )
        fig.add_trace(
            go.Pie(
                labels=['Deaths_country', 'Globally_deaths'],
                values=[max(sub_state[deaths]),
                        groupmax()['Cumulative_deaths'].sum()],
                name=cases,
                textinfo='label+percent',
                insidetextorientation='auto',
                pull=[0, 0.1],
                hole=.2
            ), 3, 2
        )
        fig.add_trace(
            go.Table(
                header=dict(values=[
                    "Date<br>report", "Code country",
                    "Country Names", "Region",
                    "New<br>cases",
                    "Cumulative<br>cases",
                    "New<br>deaths",
                    "Cumulative<br>deaths"
                ],
                    fill_color='royalblue',
                    font=dict(color='white', size=14),
                    align="center"),
                cells=dict(values=[sub_state[k][::-1].tolist() for k in
                                   sub_state.columns[1:]],
                           align="left"
                           ),
            ),
            row=4, col=1
        )
        return fig
    else:
        print(f'Source country to build reports')


@app.callback(Output('sunburst', 'figure'),
              [Input("btn_cases", "n_clicks_timestamp"),
               Input("btn_deaths", "n_clicks_timestamp"),
               Input('date_picker', 'start_date'),
               Input('date_picker', 'end_date')]
              )
def update_graph_date(btn_cases, btn_deaths, start_date, end_date):
    """
    func update data in graph sunburst if btn_cases,btn_deaths on_clicks
    and choice date_picker (start_date, end_date)
    :param btn_cases:
    :param btn_deaths:
    :param start_date:
    :param end_date:
    :return: figure for cases or deaths
    """
    if btn_cases > btn_deaths:
        fig = px.sunburst(region_hrnlg(start_date, end_date),
                          path=['WHO_region', 'Country'],
                          values=cases,
                          color='WHO_region'
                          )
        return fig
    elif btn_deaths > btn_cases:
        fig = px.sunburst(region_hrnlg(start_date, end_date),
                          path=['WHO_region', 'Country'],
                          values=deaths,
                          color='WHO_region'
                          )
        return fig


@app.callback(
    Output("map_covid_date", "figure"),
    [Input("btn_cases", "n_clicks_timestamp"),
     Input("btn_deaths", "n_clicks_timestamp"),
     Input('date_picker', 'start_date'),
     Input('date_picker', 'end_date')]
)
def update_scatter_chart(btn_cases, btn_deaths, start_date, end_date):
    """
    func update data in graph map_covid_date if btn_cases,btn_deaths on_clicks
    and choice date_picker (start_date, end_date)
    :param btn_cases:
    :param btn_deaths:
    :param start_date:
    :param end_date:
    :return: fig for cases or deaths
    """
    if btn_cases > btn_deaths:
        fig = px.choropleth(WHOreg_scat(start_date, end_date),
                            locationmode="country names",
                            locations="Country",
                            scope="world",
                            color=cases,
                            hover_name="Country",
                            hover_data=['Date_reported', cases],
                            animation_frame='Date_reported',
                            color_continuous_scale=px.colors.sequential.Blues)
        fig.update_layout(
            margin=dict(l=20, r=0, b=0, t=70, pad=0),
            paper_bgcolor="white",
            title_text=f"Statistics of cases of coronovirus "
                       f"infection in the world",
            height=700, font_size=12
        )
        return fig
    elif btn_deaths > btn_cases:
        fig = px.choropleth(WHOreg_scat(start_date, end_date),
                            locationmode="country names",
                            locations="Country",
                            scope="world",
                            color=deaths,
                            hover_name="Country",
                            hover_data=['Date_reported', deaths],
                            animation_frame='Date_reported',
                            color_continuous_scale=px.colors.sequential.Reds)
        fig.update_layout(
            margin=dict(l=20, r=0, b=0, t=70, pad=0),
            paper_bgcolor="white",
            title_text=f"Coronovirus deaths statistics in the world",
            height=700, font_size=12
        )
        return fig
