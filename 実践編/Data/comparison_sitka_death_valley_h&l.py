import csv
from datetime import datetime
import matplotlib.pyplot as plt

sitka_filename = "Data\data\sitka_weather_2018_simple.csv"
with open(sitka_filename) as sf:
    sf_reader = csv.reader(sf)
    header_row = next(sf_reader)
    # print(f"sitka:{header_row}")

    sf_dates, sf_highs, sf_lows = [], [], []
    for sf_row in sf_reader:
        current_date = datetime.strptime(sf_row[2], "%Y-%m-%d")
        high = int(sf_row[5])
        low = int(sf_row[6])
        sf_dates.append(current_date)
        sf_highs.append(high)
        sf_lows.append(low)

death_valley_filename = "Data\data\death_valley_2018_simple.csv"
with open(death_valley_filename) as df:
    df_reader = csv.reader(df)
    header_row = next(df_reader)
    # print(f"death_valley:{header_row}")

    df_dates, df_highs, df_lows = [], [], []
    for df_row in df_reader:
        current_date = datetime.strptime(df_row[2], "%Y-%m-%d")
        try:
            high = int(df_row[4])
            low = int(df_row[5])
        except ValueError:
            print(f"{current_date}日のデータがありません")
        else:
            df_dates.append(current_date)
            df_highs.append(high)
            df_lows.append(low)

plt.style.use("classic")
fig, ax = plt.subplots()

ax.plot(sf_dates, sf_highs, c="red")
ax.plot(sf_dates, sf_lows, c="red")
plt.fill_between(sf_dates, sf_highs, sf_lows, facecolor="red", alpha=0.1)

ax.plot(df_dates, df_highs, c="blue")
ax.plot(df_dates, df_lows, c="blue")
plt.fill_between(df_dates, df_highs, df_lows, facecolor="blue", alpha=0.1)

# グラフにフォーマットを指定する
plt.title("Comparison sitka/deathvalley h&l - 2018", fontsize=24)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()
