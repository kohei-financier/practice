from plotly.graph_objects import Bar, Layout
from plotly import offline

from die import Die

die1 = Die()
die2 = Die()
# die3 = Die()

# サイコロを転がし、結果をリストに格納する
results = [die1.roll() + die2.roll() for roll_num in range(100000)]
# for roll_num in range(100000):
#     result = die1.roll() * die2.roll()
#     results.append(result)

# 結果を分析する
max_result = die1.num_sides + die2.num_sides
frequencies = [results.count(value) for value in range(2, max_result + 1)]
# for value in range(1, max_result + 1):
#     frequency = results.count(value)
#     frequencies.append(frequency)

x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title": "結果", "dtick": 1}
y_axis_config = {"title": "発生した回数"}

my_layout = Layout(
    title=f"{die1.num_sides}面・{die2.num_sides}面のサイコロを{len(results)}回転がした結果",
    xaxis=x_axis_config,
    yaxis=y_axis_config,
)

offline.plot(
    {"data": data, "layout": my_layout},
    filename=f"d{die1.num_sides}_d{die2.num_sides}.html",
)
