import matplotlib.pyplot as plt

x_values = range(1, 1000)
y_values = [x**3 for x in x_values]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)


#グラフのタイトルと軸のラベルを設定する
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#各軸の範囲を設定する
ax.axis([0, 1100, 0, 1100000000])


plt.show()
