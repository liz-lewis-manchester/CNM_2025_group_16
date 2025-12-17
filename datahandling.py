#extract the data from each column into an array and use the flatten function to convert data into 1-dimensional
def read_data(length, spatial_resolution, filename):
    df = pd.read_csv(filename, encoding='latin1')#use encoding='latin1' because the symbol mu cannot be read
    return df[['Concentration (µg/m_ )']].values.flatten()
    #return concentration list

def interpolation(length, spatial_resolution, conc_list, distance_list):
    distance_grid = np.arange(0, length + spatial_resolution, spatial_resolution) 
    conc_grid = np.interp(distance_grid, distance_list, conc_list)
    return conc_grid, distance_grid
conc_raw, distance_raw = read_data(20, 0.2, 'initial_conditions.csv') #example values for conc_list, distance_list parameters
#print(interpolation(20,0.2, conc_raw, distance_raw))
