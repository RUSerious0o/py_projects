import pandas
import pandas_ta
import yfinance as yf


def fetch_stock_data(ticker, period='1mo'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def add_rsi(data: pandas.DataFrame, length: int = 14) -> pandas.DataFrame:
    """
        Добавляет к данным информацию о техническом индикаторе RSI

    :param data: pandes.DataFrame, данные об акциях за период
    :param length: int, расчетный период индикатора, в днях (рекомендуются: 9, 14, 25)
    :return: data: pandas.DataFrame, дополненные индикатором PSI данные об акциях за период
    """

    data['RSI'] = pandas_ta.rsi(data['Close'], length=length)
    return data
