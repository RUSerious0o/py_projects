import data_download
import data_plotting as dplt
import time
from utils import *


def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print("Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")
    print("                                     Соответственно: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max")

    ticker = input("\nВведите тикер акции (например, «AAPL» для Apple Inc):»")

    invalid_input = True
    while invalid_input:
        input_msg = "Введите период для данных (например, '1mo' для одного месяца) или границы периода (например: 2024-01-01 2024-04-20): "
        user_input = parse_period_input(input(input_msg))
        invalid_input = not user_input['input_is_valid']

    invalid_input = True
    while invalid_input:
        input_msg = ("Выберите стиль оформления графика:\n"
                     "1 - стиль по умолчанию, 2 - график на темном фоне, 3 - с сеткой на сером фоне: ")
        plot_style = input(input_msg)
        try:
            plot_style = int(plot_style) - 1
            if plot_style in range(3):
                invalid_input = False
        except:
            pass


    # Fetch stock data
    stock_data = data_download.fetch_stock_data(ticker, user_input['period'], user_input['start'], user_input['end'])

    # Add moving average to the data
    stock_data = data_download.add_moving_average(stock_data)

    # Add std deviation to the data
    stock_data = data_download.add_std_deviation(stock_data)

    # Add RSI to the data
    stock_data = data_download.add_rsi(stock_data)

    # Plot the data
    dplt.create_and_save_plot(stock_data, ticker, period=user_input['period'], style_num=plot_style)

    # View average price
    calculate_and_display_average_price(stock_data)

    # View interactive plot
    dplt.show_interactive_plot(stock_data, ticker)

    # Strong fluctuations test
    notify_if_strong_fluctuations(stock_data, 10.5)
    notify_if_strong_fluctuations(stock_data, 3.1)

    # Write data to csv file
    export_data_to_csv(stock_data, 'stock_data.csv')


def parse_period_input(user_input: str) -> dict:
    result = {
        'input_is_valid': False,
        'period': None,
        'start': None,
        'end': None
    }

    valid_periods = ('1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max')
    if user_input in valid_periods:
        result['input_is_valid'] = True
        result['period'] = user_input

    try:
        start_date, end_date = user_input.split()
        valid_date = time.strptime(start_date, '%Y-%m-%d')
        valid_date = time.strptime(end_date, '%Y-%m-%d')

        result['input_is_valid'] = True
        result['start'] = start_date
        result['end'] = end_date

    except ValueError:
        return result

    return result


if __name__ == "__main__":
    main()
