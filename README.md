# CNM_2025_group_16

Make sure we always make a new branch and code on and commit changes to that before we merge. Try describe each commit as accurately as possible and comment on each others changes as much as we can. Comments and documentation on our own code is a good idea i think and we can always remove extra stuff later so don't limit yourself imo. also if a value can be passed in (unless its for the central script) instead of hard coded just make it a parameter and we can edit later.


Tasks:

- central script that runs all other scripts as needed with possibly a function per test case. mostly just calls functions from other scripts and passes outputs from them as inputs into the next. this is the only file that relies on other people (what they've called their functions and how theyve set out their parameters)
  
- a python script with a function to read in initial conditions and format/store (use pandas) and a function to interpolate data so theres enough data points (this may be the initial condition data or something else so it must be flexible and allow for the central script to pass in the data)
  
- script that uses the advection equation to find concentrations at different points:
    - takes in a set of initial concentrations along the river (may or may not be the initial conditions file so again flexibility including over the length of the river/ list of concentrations needed) and outputs multiple concentration-distance lists
    - the finite differences method just approximates the derivative and finds the difference between the concentration at two adjacent data points along the river (dθ/dx) and then puts that into the given advection equation to find the next value for that distance
    - dx and dt are defined by us or the coursework. just the spatial and temporal resolutions
    - so dθ/dx becomes: (θ at position n) - (θ at position n-1)/spatial resolution and its similar for θ at diff points in time - just rearrange to get θ at the next time step and loop through that function to get more steps and the concentrations along the river for each of those new time steps
      
- script that takes the data from the finite differences script (lists of concentrations and distances) to produce data plots showing the pollution at a specific time step (one graph per time step - theres gonna be many being generated if its over 5 minutes like in test 1 - the output gets updated so you can see the changing river)
    -this will need to take arguments from the central script so it can complete different tests so it needs to be flexible enough that different values like temporal resolution, U etc can be used


All scripts go in src, initial conditions is in data, im guessing tests is for like along the way and we need to save the actual final figures in results. once we're done we need to describe folder structure in this README file properly.

also please add to and change this as much as you want - if anyone knows how to get jupyter notebooks in the notebooks/ section that'd be really helpful cos ive been using vsc up until now so that ones new to me
