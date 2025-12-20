import pandas as pd
import numpy as np
# extract the data from each column into an array and use the flatten function to convert data into 1-dimensional
def read_data(length, spatial_resolution, filename):
    df = pd.read_csv(filename) # use encoding='latin1' because the symbol mu cannot be read
    conc_list = df[['Concentration (μg/m_ )']].values.flatten() 
    distance_list = df[['Distance (m)']].values.flatten() 
    n_data = len(conc_list) # number of data points in the file
    distance_grid = np.arange(0, length + spatial_resolution, spatial_resolution, dtype=float)
    n_grid = len(distance_grid)
    # decide if interpolation is necessary
    if n_data == n_grid:
        conc = conc_list
        distance = distance_list
    else:
      conc = np.interp(distance_grid, distance_list, conc_list)
      distance = distance_grid
    return conc, distance

# test with example values
# conc, distance, n_data = read_data(20, 0.2, 'initial_conditions.csv')
#print(conc)
#print(distance)
#print(n_data)
