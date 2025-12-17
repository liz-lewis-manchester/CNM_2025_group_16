import pandas as pd
import numpy as np
def main(length,spatial_res,temp_res,init_conc,vel,pos_0_conc): #base function that calls on .. and creates outputs
    return #vel and pos_0_conc can be a single value or list
    
#extract the data from each column into an array and use the flatten function to convert data into 1-dimensional
def read_data(length, spatial_resolution, filename):
    df = pd.read_csv(filename, encoding='latin1')#use encoding='latin1' because the symbol mu cannot be read
    return df[['Concentration (µg/m_ )']].values.flatten()
    #return concentration list

def interpolation(length, spatial_resolution, conc_list, distance_list):
    distance_grid = np.arange(0, length + spatial_resolution, spatial_resolution)
    conc_grid = np.interp(distance_grid, distance_list, conc_list)
    return conc_grid, distance_grid
conc_raw, distance_raw = read_data(20, 0.2, 'initial_conditions.csv')
#print(read_data(20, 0.2, 'initial_conditions.csv'))
print(interpolation(20,0.2, conc_raw, distance_raw))

def test_initial_conditions_file(length,spatial_res,filename,in_conc):
#    file_data = get_data(filename,length,spatial_res) #call function from .. script to get initial concentrations list
#    main(length,spatial_res,10,file_data,0.1,in_conc)
    return

def test_sensitivity():
    length = 2000
    vel_list = [0.05,0.1,0.2,0.5,1,4,50,200]
    spatial_res_list = [0.01,0.1,0.2,0.5,1,2,20,50]
    temp_res_list = [1,5,10,20,50,100,180] #lists of possible tests on paramters to check sensitivity
    for vel in vel_list:
        for spatial_res in spatial_res_list:
            for temp_res in temp_res_list:
                divisions = length/spatial_res
                main(length,spatial_res,temp_res,[250,0 for i in range(divisions)],vel,0.2)

def test_exponential_decay(): #create exponential list to use as pos 0 concentration list (at the start of stream)
    return

def test_variable_stream_velocity(): #create list of velocities that arent constant all the way through
    return

#run each test
main(20,0.2,10,[250,0 for i in range(100)],0.1,0)
test_initial_conditions_file(20,0.2,"initial_conditions.csv",[])
test_sensitivity()
test_exponential_decay()
test_variable_stream_velocity()
