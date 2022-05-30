import pandas as pd
import streamlit as st
import plotly.express as px


def streamlit_2columns_metrics_df_shape(df: pd.DataFrame):
    (
        column1name,
        column2name,
    ) = st.columns(2)

    with column1name:
        st.metric(
            label="Rows",
            value=df.shape[0],
            delta=None,
            delta_color="normal",
        )

    with column2name:
        st.metric(
            label="Columns",
            value=df.shape[1],
            delta=None,
            delta_color="normal",
        )


def show_inputted_dataframe(data):
    with st.expander("Input Dataframe (X and y)"):
        st.dataframe(data)
        streamlit_2columns_metrics_df_shape(data)


def standard_decomposition_plot(decomposition):

    fig = decomposition.plot()

    (xsize_standard_decomp, ysize_standard_decomp) = streamlit_chart_setting_height_width(
        "Chart Settings", 5, 5, "xsize_standard_decomp", "ysize_standard_decomp")

    fig.set_size_inches(xsize_standard_decomp, ysize_standard_decomp)

    st.pyplot(fig)


def time_series_line_plot(data):
    fig = px.line(
        data
    )
    st.plotly_chart(fig, use_container_width=True)


def time_series_scatter_plot(data):
    fig = px.scatter(
        data
    )
    st.plotly_chart(fig, use_container_width=True)


def time_series_box_plot(data):
    fig = px.box(data, points="all")
    st.plotly_chart(fig, use_container_width=True)


def time_series_line_and_box(data):

    with st.expander("Line plot"):
        time_series_line_plot(data)

    with st.expander("Box plot"):
        time_series_box_plot(data)


def streamlit_chart_setting_height_width(
    title: str,
    default_widthvalue: int,
    default_heightvalue: int,
    widthkey: str,
    heightkey: str,
):
    with st.expander(title):

        lbarx_col, lbary_col = st.columns(2)

        with lbarx_col:
            width_size = st.number_input(
                label="Width in inches:",
                value=default_widthvalue,
                key=widthkey,
            )

        with lbary_col:
            height_size = st.number_input(
                label="Height in inches:",
                value=default_heightvalue,
                key=heightkey,
            )
    return width_size, height_size
