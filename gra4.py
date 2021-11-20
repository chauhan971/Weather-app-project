import matplotlib.pyplot as plt

# x axis values
x = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11]
# corresponding y axis values
y = [172,174,166,149,124,108,101,107,123,162]

# plotting the points
plt.plot(x, y, color='green', linestyle='dashed', linewidth=3,
         marker='o', markerfacecolor='blue', markersize=12)

# setting x and y axis range
plt.ylim(1, 500)

# naming the x axis
plt.xlabel('Date')
# naming the y axis
plt.ylabel('AQI - Level')

# giving a title to my graph
plt.title('AQI - Level of Shimla!')

# function to show the plot
plt.show()