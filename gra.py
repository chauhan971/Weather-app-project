import matplotlib.pyplot as plt

x = [10, 12, 14, 16, 18, 20, 22, 24, 26, 27]
y = [269, 212, 163, 64, 301, 927, 576, 496, 672, 387]

plt.plot(x, y, color='green', linestyle='dashed', linewidth=3,
         marker='o', markerfacecolor='blue', markersize=12)

plt.ylim(1, 1000)

plt.xlabel('Date')

plt.ylabel('AQI - Level')

plt.title('AQI - Level of Delhi!')

plt.show()