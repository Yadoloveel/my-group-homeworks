import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from appcovd import app
from layouts import main_page, pgstat_layout, pghronolog_layout


url_bar_and_content_div = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# index layout
app.layout = url_bar_and_content_div

# complete layout
app.validation_layout = html.Div([
    url_bar_and_content_div,
    main_page,
    pgstat_layout,
    pghronolog_layout,
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    """
    func for updates the web pages with url
    :param pathname:
    :return: main_page, pgstat_layout or pghronolog_layout
    """
    if pathname == '/pgstat':
        return pgstat_layout
    elif pathname == '/pghronolog':
        return pghronolog_layout
    else:
        return main_page


if __name__ == '__main__':
    app.run_server(debug=True, threaded=False)
