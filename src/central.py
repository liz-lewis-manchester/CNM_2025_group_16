from datahandling import read_data
from calculations import advection_model
from plotting import plot_graphs

import random
import math as mt

def main(length,time, spatial_res,temp_res,init_conc,vel,pos_0_conc = None, test_num = 0): #base function that calls on .. and creates outputs
    for i in range(len(init_conc)):
        init_conc[i] = float(init_conc[i])

    datapoints = length/spatial_res + 1
    
    data_grid = advection_model(init_conc, length, time, int(datapoints), int(time/temp_res) +1, vel, pos_0_conc) #vel and pos_0_conc can be a single value or list
    plot_graphs(data_grid, length, time, spatial_res, temp_res,test_num)

def test_initial_conditions_file(length, time, spatial_res,temp_res, vel, filename,input_conc = None):
    conc_list, dist_list =  read_data(length,spatial_res,filename) #call function from .. script to get initial concentrations list
    main(length,time,spatial_res,temp_res,conc_list,vel,input_conc,2)

def test_sensitivity():
    length = 2000
    time = 120
    input_conc = 200
    vel_list = [0.05,0.5,200]
    spatial_res_list = [0.01,0.5,50]
    temp_res_list = [1,5,30] #lists of possible tests on paramters to check sensitivity
    for vel in vel_list:
        for spatial_res in spatial_res_list:
            for temp_res in temp_res_list:
                dist_div = int(length/spatial_res)+1
                time_div = int(time/temp_res)+1
                list1 = []
                list1.append(250)
                for i in range(100):
                    list1.append(0)
                main(length,time,spatial_res,temp_res,list1,[vel for i in range(dist_div)],[input_conc for i in range(time_div)],3)

def test_exponential_decay(time, temp_res, start): #create exponential list to use as pos 0 concentration list (at the start of stream)
    steps = time/temp_res + 1
    input_conc_list = []
    max = mt.exp(steps)
    for i in range(int(steps)):
        input_conc_list.append(float(start - (mt.exp(i)*start)/max))
    return input_conc_list


def test_variable_stream_velocity(length, spatial_res, base_vel): #create list of velocities that arent constant all the way through
    points = length/spatial_res + 1
    vel_list = []
    for i in range(int(points)):
        vel_list.append(base_vel*(1+(random.randrange(-10,10)/100)))
    return vel_list

#run each test
list1 = []
list1.append(250)
for i in range(100):
    list1.append(0)

main(20,300,0.2,10,list1,[0.1 for i in range(101)],[250 for i in range(31)],1) #test cases
test_initial_conditions_file(20,300,0.2,10, [0.1 for i in range(101)],"data/initial_conditions.csv",[250 for i in range(31)])


input_list = test_exponential_decay(300, 10, 400)

list2 = []
list2.append(400)
for i in range(100):
    list2.append(0)
main(20,300,0.2,10,list2,[0.1 for i in range(101)],input_list,4)


vel_list = test_variable_stream_velocity(300,10,0.1)
main(20,300,0.2,10,list1,vel_list,None,5)

test_sensitivity()
