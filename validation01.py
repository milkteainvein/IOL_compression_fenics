import numpy as np
import csv 

def calculate_decentration(x_coordinates, data, n, array):
    # Split into x and y
    x = data[:, 0]
    y = data[:, 1]

    # Fit linear model: y = mx + b
    coeffs = np.polyfit(x, y, deg=1)  # coeffs[0] = m, coeffs[1] = b

    # Generate fitted line
    y_fit = coeffs[0] * x + coeffs[1]

    # create an array to hold the calculated y-values
    y_values = [0]
    for i in range(3):
        x_new = x_coordinates[i][n]
        y_new = coeffs[0] * x_new + coeffs[1]
        y_values.append(y_new)
    
    return y_values


# make a list to store the values in
generated_data = [ [0,6.5986,9.78,11.0762],[0,0.38,0.49,0.55]]

# read the x coordinates
with open("./data_sheet_paper_3/x_values.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.reader(file)
    x_coordinates = list(reader)
x_coordinates = np.array(x_coordinates, dtype=float)

# read in each seperate data set
for i in range(1, 7):
    with open(f"./data_sheet_paper_3/{i}.csv", "r", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        data = list(reader)
    data = np.array(data, dtype=float)
    generated_data.append(calculate_decentration(x_coordinates, data, i-1, array=generated_data))

generated_data = np.array(generated_data).T
print(generated_data)

with open("./plot/y_values.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(generated_data)
