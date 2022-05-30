import statsmodels.api as sm
import pandas as pd
import streamlit as st

model_types = ['Additive', 'Multiplicative']


def decompose_time_series(data):
    selected_model_type = st.radio(
        'Model type:', model_types)
    decomposition = sm.tsa.seasonal_decompose(
        data, model=selected_model_type.lower())
    return [decomposition, selected_model_type]


def extract_trend_seasonal_resid(decomposition):
    trend = decomposition.trend
    seasonal = decomposition.seasonal
    residual = decomposition.resid

    return [trend, seasonal, residual]


def create_trend_seasonal_df(trend, seasonal):
    frame = {'Trend': trend, 'Seasonal': seasonal}
    return pd.DataFrame(frame)
