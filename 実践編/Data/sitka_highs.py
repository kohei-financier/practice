import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = "Data\data\sitka_weather_2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # ファイルから日付と最高気温を取得する
    dates, precipitations, highs, lows = [], [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        current_precipitation = float(row[3])
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        precipitations.append(current_precipitation)
        highs.append(high)
        lows.append(low)

# 最高気温のグラフを描画する
plt.style.use("classic")
fig, ax = plt.subplots()
# ax.plot(dates, highs, c="red", alpha=0.5)
# ax.plot(dates, lows, c="blue", alpha=0.5)
ax.plot(dates, precipitations, c='green')
# plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

# グラフにフォーマットを指定する
plt.title("Daily precipitations and temperatures - 2018", fontsize=24)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
# plt.ylabel("Temperature (F)", fontsize=16)
plt.ylabel("Precipitations(m)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()
