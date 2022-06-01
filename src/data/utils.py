import pandas as pd
data_set_options = [
    'Airline',
    'Milk production'
]


def import_sample_data(sample_data_selected, data_set_options):
    if sample_data_selected == data_set_options[0]:
        data = pd.read_csv('data/processed/airline.csv',
                           parse_dates=['Month'], index_col='Month')

    if sample_data_selected == data_set_options[1]:
        data = pd.read_csv('data/processed/milk_production.csv',
                           parse_dates=['date'], index_col='date')

    graph_data = data.reset_index()
    graph_data.columns.values[0] = 'Date'
    return data, graph_data
