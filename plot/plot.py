import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import csv

np.set_printoptions(precision=5, suppress=True)
mpl.rcParams['axes.linewidth'] = 2

def plot_data(x_coordinates, y_coordinates):
  # set the different markers we want to use for the data points.
  markers = ['o', 's', '^', '*', 'X', 'D', 'p']
  names = ["Clinical data", 1, 2, 3, 4, 5, 6]

  # plot each line
  for i in range(len(y_coordinates)):
    plt.plot(x_coordinates, y_coordinates[i], marker = markers[i])
  
  # add the title, xlabel, ylabel and save to the png.
  plt.title("Clinical validation of decentration")
  plt.xlabel("Contraction rate (%)")
  plt.ylabel("IOL decentration (mm)")
  plt.grid()
  plt.legend(names)
  plt.savefig("plot.png")
  plt.close()


# import the data
with open("y_values.csv", "r", encoding="utf-8-sig") as file:
  reader = csv.reader(file)
  data = list(reader)
data = np.array(data, dtype=float)

# take out the x_coordinates and the y_coordinates
x_coordinates = data[:, :1]
y_coordinates = np.array([data[:,n] for n in range(1, len(data[1, :]))])


plot_data(x_coordinates, y_coordinates)