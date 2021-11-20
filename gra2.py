import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11]
y = [94,109,102,154,95,138,134,131,138,124]

plt.plot(x, y, color='green', linestyle='dashed', linewidth=3,
         marker='o', markerfacecolor='blue', markersize=12)

plt.ylim(1, 500)

plt.xlabel('Date')

plt.ylabel('AQI - Level')

plt.title('AQI - Level of Mumbai!')

plt.show()
