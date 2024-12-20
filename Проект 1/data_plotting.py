import matplotlib.pyplot as plt
import pandas as pd


def create_and_save_plot(data, ticker, period, filename=None, style_num=0):
    plt.figure(num=1, figsize=(12, 12))

    styles = ('default', 'dark_background', 'ggplot')
    plt.style.use(styles[style_num])

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.subplot(2, 1, 1)
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
            plt.plot(dates, data['RSI'].values, label='RSI')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')

    plt.title(f"{ticker} Цена акций с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(dates, data['Std_Deviation'].values, label='Std Deviation')
    plt.title('Стандартное отклонение цены закрытия акций')
    plt.xlabel('Дата')
    plt.ylabel('Величина отклонения')


    if filename is None:
        filename = f"{ticker}_{period if period else 'period'}_stock_price_chart.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")
