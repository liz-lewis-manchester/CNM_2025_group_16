# Group 16: River Pollution Advection Model

This code simulates the evolution of a pollutant concentration in a river using an advection equation. Starting from an initial concentration profile along the river, the model calculates how pollution moves and and produces plots showing how pollutant concentration changes with time and distance. 

The code is setup with modules: data handling, calculations, plotting. A central script controls how the full simulation is run. 

## Function of the code
1. Read initial pollution concentrations along a river from a data file
2. Interpolates said data to create an evenly spaced spatial grid
3. Solves the advection equation using a finite difference method to simulate pollution movement over time
4. Produces plots showing pollution concentration along the river
5. Final figures show the results of the simulation, saved for later analysis

## Use of the code
First prepare initial conditions - place the pollution data in the data folder. The data should contain concentration values along the length of the river. 

All simulations are run from the central script, where the parameter are identified and need to be defined. 
When the simulation is executed, the script with load and process inital data, interpolate it, solve the advection equation and generates concentration profiles. 

## Code Structure
/data - initial condition files

/src - main python scripts including: datahandling.py, calculations.py, dataplots.py and central.py

/results - saved output figures

/tests - testing of the code
