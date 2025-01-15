import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

plt.style.use("dark_background")
"""
['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', 
'_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background',
'fast', 'fivethirtyeight', 'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark',
'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid', 'seaborn-v0_8-deep',
'seaborn-v0_8-muted','seaborn-v0_8-poster', 'seaborn-v0_8-talk',
'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid',
'tableau-colorblind10']
"""
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# グラフのタイトルと軸のラベルを設定する
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# 目盛りラベルのサイズを設定する
ax.tick_params(axis="both", labelsize=14)

plt.show()
