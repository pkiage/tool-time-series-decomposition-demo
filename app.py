import streamlit as st
import pandas as pd
from src.data.utils import *
from src.visualization.visualize import *
from src.features.build_features import *


def main():

    st.title("Time Series Decomposition Demo")

    st.header("Data")

    sample_data_selected = st.selectbox(
        'Select sample data:', data_set_options)

    data, graph_data = import_sample_data(
        sample_data_selected, data_set_options)

    show_inputted_dataframe(data)

    with st.expander("Box Plot:"):
        time_series_box_plot(graph_data)

    with st.expander("Dist Plot (histogram and violin plot):"):
        time_series_violin_and_box_plot(data)

    st.header("Time series decomposition")

    [decomposition, selected_model_type] = decompose_time_series(data)

    if selected_model_type == model_types[0]:
        st.subheader('Additive Model')
        st.latex(r'''
        Y[t] = T[t]+S[t]+e[t]
        ''')

    if selected_model_type == model_types[1]:
        st.subheader('Multiplicative Model')
        st.latex(r'''
        Y[t] = T[t] \times S[t] \times e[t]
        ''')

    standard_decomposition_plot(decomposition)

    [trend, seasonal, residual] = extract_trend_seasonal_resid(decomposition)

    with st.expander("Time series Line Plot (Y[t])"):
        time_series_line_plot(data)

    st.latex(r'''=''')

    with st.expander("Trend Plot (T[t])"):
        st.write('The trend component of the data series.')
        st.write('Trend: secular variation(long-term, non-periodic variation)')

        time_series_line_plot(trend)

    if selected_model_type == model_types[0]:
        st.latex(r'''+''')

    if selected_model_type == model_types[1]:
        st.latex(r'''\times''')

    with st.expander("Seasonality Plot (S[t])"):
        st.write('The seasonal component of the data series.')
        st.write(
            'Seasonality: Periodic fluctuations (often at short-term intervals less than a year).')
        time_series_line_plot(seasonal)

    if selected_model_type == model_types[0]:
        st.latex(r'''+''')

    if selected_model_type == model_types[1]:
        st.latex(r'''\times''')

    with st.expander("Residual Plot (e[t])"):
        st.write('The residual component of the data series.')
        st.write('Residual: What remains after the other components have been removed (describes random, irregular influences).')
        st.write(f'Residual mean: {residual.mean():.4f}')
        time_series_scatter_plot(residual)


if __name__ == "__main__":
    main()
