import matplotlib.pyplot as plt

def plot_graphs(data_grid, length, time, spatial_res, temp_res):   ## Define a function to plot concentration profiles over time
    time_steps = int(time/temp_res)      ##number of time steps based on total time and time resolution
    dist_steps = int(length/spatial_res)    ##number of spatial steps based on river length and spatial resolution
    dist_list = []
    figures = [[] for i in range(time_steps)]  ## Create a list of empty lists to store saved figure references for each time step
    for i in range(dist_steps):   ##loop
        dist_list.append(i*spatial_res)
    for i in range(time_steps):   ##loop
        plt.title = "Concentration Profile at t =",time_steps*temp_res,"s"
        plt.plot(dist_list,data_grid[i])     ### Plot concentration versus distance for the current time step
        plt.xlabel('Distance along river(m)')
        plt.ylabel('Concentration µg/m^3')
        plt.draw()
        figures[i].append(plt.savefig('t'+str(i)+'.png'))
        plt.pause(1)
        plt.cla()
    return figures
