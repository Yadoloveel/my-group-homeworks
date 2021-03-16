import pandas as pd
import dash_core_components as dcc
import json


def urlcsv():
    """
    read_csv file from site who.int and save to data/WHO_global_data.csv
    :return: None
    """
    df_urlcsv = pd.read_csv(
                         'https://covid19.who.int/WHO-COVID-19-global-data.csv'
                         )
    df_urlcsv.to_csv(r'data/WHO_global_data.csv', index=False)
    # return None


# global df from 'data/WHO_global_data.csv'-----
df_csv = pd.read_csv('data/WHO_global_data.csv')
df = df_csv.copy(deep=True)

# Open data/countries.geo.json counties for graph all_covid_map
with open('C:/Users/nglaz/PycharmProjects/dash_covid_laz/data/'
          'countries.geo.json') as response:
    counties = json.load(response)


def groupmax():
    """
    Create query df by country with value max()
    :return: country
    """
    country = df.groupby(['Country']).max().reset_index()
    return country


def space_num(number):
    """
    Create space_number for allsumhead
    :param number
    :return: prob
    """
    prob = f"{number:,}".replace(',', ' ')
    return prob


def allsumhead():
    """
    Create head_page cases & deaths for header_allpages
    :return: header
    """
    cases = space_num(groupmax()['Cumulative_cases'].sum())
    deaths = space_num(groupmax()['Cumulative_deaths'].sum())
    header = dcc.Markdown(f"#### At **{date_head()}**, globally, there have "
                          f"been confirmed cases of (COVID-19) - **{cases}**, "
                          f"including - _**{deaths}**_ deaths.")
    return header


def region_stat():
    """
    Create df WHO_region by 'WHO_region','Country' for graph treemap main_page
    :return: region
    """
    region = df.groupby(['WHO_region', 'Country']).agg(
        {'Cumulative_cases': ['max'],
         'Cumulative_deaths': ['max']})
    region.columns = ['Cumulative_cases', 'Cumulative_deaths']
    region.reset_index(inplace=True)
    return region


def region_main():
    """
    Create df WHO_region for graph barh on main_page
    :return: region
    """
    region = df.groupby(['WHO_region', 'Date_reported']).agg(
        {'Cumulative_cases': ['max'],
         'Cumulative_deaths': ['max']})
    region.columns = ['Cumulative_cases', 'Cumulative_deaths']
    region.reset_index(inplace=True)
    return region


def subplt_country(dd_country):
    """
    Query df Country for subplots-graph page_statistic1
    :param dd_country:
    :return: country
    """
    country = df[df['Country'] == dd_country]
    country.reset_index(inplace=True)
    return country


def topScatter1(sub_state):
    """
    Query New_cases on topScatter graph for subplots-graph page_statistic1
    :param sub_state:
    :return: Newcas
    """
    newcas = sub_state[max(sub_state['Date_reported']) ==
                       sub_state['Date_reported']].reset_index()
    newcas = newcas['New_cases'][0]
    return newcas


def topScatter2(sub_state):
    """
    Query New_deaths on topScatter graph for subplots-graph page_statistic1
    :param sub_state:
    :return: Newdeth
    """
    newdeth = sub_state[max(sub_state['Date_reported']) ==
                        sub_state['Date_reported']].reset_index()
    newdeth = newdeth['New_deaths'][0]
    return newdeth


def region_hrnlg(start_date, end_date):
    """
    Create df WHO_region by 'WHO_region','Country'
    for graphs sunburst page_horology1 with DatePickerRange
    :param start_date:
    :param end_date:
    :return: hrnlg1
    """
    hrnlg1 = WHOreg_scat(start_date, end_date)
    hrnlg1 = hrnlg1.groupby(['WHO_region', 'Country']).agg(
        {'Cumulative_cases': ['max'],
         'Cumulative_deaths': ['max']})
    hrnlg1.columns = ['Cumulative_cases', 'Cumulative_deaths']
    hrnlg1.reset_index(inplace=True)
    return hrnlg1


def WHOreg_scat(start_date, end_date):
    """
    Create df WHO_region by 'WHO_region','Country'
    for graphs map_covid_date page_hronolog2 with DatePickerRange
    :param start_date:
    :param end_date:
    :return: whoreg
    """
    whoreg = df[(df['Date_reported'] >= start_date) &
                (df['Date_reported'] <= end_date)]
    return whoreg


def data_report():
    """
    Convected to_datetime Date_reported for map_covid_date on page_hronolog2
    :return: df_date
    """
    df_date = pd.to_datetime(df['Date_reported'])
    return df_date


def date_head():
    """
    Create last date reported form df head on main_page
    :return: df_dnow
    """
    df_dnow = f"{max(pd.to_datetime(df['Date_reported'])): %d %B %Y}"
    return df_dnow
