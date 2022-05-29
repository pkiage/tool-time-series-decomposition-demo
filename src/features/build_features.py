import statsmodels.api as sm
import pandas as pd


def decompose_time_series(data):
    return sm.tsa.seasonal_decompose(data)


def extract_trend_seasonal_resid(decomposition):
    trend = decomposition.trend
    seasonal = decomposition.seasonal
    residual = decomposition.resid

    return [trend, seasonal, residual]


def create_trend_seasonal_df(trend, seasonal):
    frame = {'Trend': trend, 'Seasonal': seasonal}
    return pd.DataFrame(frame)
