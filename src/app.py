import streamlit as st
import pandas as pd
from data.utils import *
from visualization.visualize import *
from features.build_features import *

import os


def main():

    st.title("Time Series Decomposition Demo")

    st.header("Data")

    sample_data_selected = st.selectbox(
        'Select sample data:', data_set_options)

    data = import_sample_data(sample_data_selected, data_set_options)

    show_inputted_dataframe(data)

    time_series_line_and_box(data)

    st.header("Time series decomposition")

    decomposition = decompose_time_series(data)

    standard_decomposition_plot(decomposition)

    [trend, seasonal, residual] = extract_trend_seasonal_resid(decomposition)

    with st.expander("Trend Plot"):
        st.write('The trend component of the data series.')
        st.write('Trend: secular variation(long-term, non-periodic variation)')

        time_series_line_plot(trend)

    with st.expander("Seasonality Plot"):
        st.write('The seasonal component of the data series.')
        st.write(
            'Seasonality: Periodic fluctuations (often at short-term intervals less than a year).')
        time_series_line_plot(seasonal)

    with st.expander("Residual Plot"):
        st.write('The residual component of the data series.')
        st.write('Residual: What remains after the other components have been removed (describes random, irregular influences).')
        st.write(f'Residual mean: {residual.mean():.4f}')
        time_series_scatter_plot(residual)


if __name__ == "__main__":
    main()
