import numpy as np

# Build coefficient arrays A and B which are used to update the concentration during time stepping

# Parameters used: 
# U - flow velocity (m/s)
# dx - spatial grid spacing
# dt - time step size
# Nx - number of spatial grid points

def coefficients(U, dx, dt, Nx):
    """
    Construct coefficient arrays used in the time-stepping update.
    """

  alpha = U * dt / dx

  # Allocate arrays for coefficients
  A = np.zeros(Nx - 1) 
  B = np.zeros(Nx - 1)
  
  # Fill in coefficient values
  # These define how each point depends on its neighbour during the update step
  for i in range(Nx -1):
    A[i] = 1 + alpha
    B[i] = alpha

  return A, B



# FUNCTION TO SOLVE ADVECTION EQUATION: dθ/dt = -U * dθ/dx using finite-difference 

# Parameters used: 
# initial_theta - initial concentration values on the spatial grid
# L - length of the model domain (m)
# T - total simulation time (s)
# Nx - number of spatial grid points
# Nt - number of time steps
# U - flow velocity (m/s) 

def advection_model(initial_theta, L, T, Nx, Nt, U):
    """
    Solve the 1D linear advection equation using a finite-difference scheme.
    """

  # Spacing in space and time
  dx = L / (Nx - 1) 
  dt = T / Nt 

  # Arrays holding the old and new concentration values
  theta_old = np.array(initial_theta, dtype=float)
  theta_new = np.zeros(Nx)

  # Coefficient arrays for the update formula
  A, B = coefficients(U, dx, dt, Nx)

  # Right-hand-side vector used when updating the solution
  F = np.zeros(Nx-2)

  # Storage for all time steps
  solutions = np.zeros((Nt, Nx))

  # Loop over time steps
  for j in range(Nt):

    # Apply boundary conditions at the upstream end (value is fixed here)
    theta_new[0] = theta_old[0]

    # Build the right-hand-side values using the previous solution
    for i in range(Nx - 2):
        F[i] = (1.0 / dt) * theta_old[i + 1]

    # Update the interior points of the domain
    # Each new value depends on the previous value and the already-updated left neighbour
    for i in range(1, Nx - 1):
        theta_new[I] = (1.0 / A[I - 1]) * (F[i - 1] - B[i - 1] * theta_new[i - 1])

    # Apply downstream boundary condition
    theta_new[-1] = theta_new[-2]

    # Save the current time step
    solutions[j, :] = theta_new.copy()

    # Prepare for next step by overwriting old values
    theta_old[:] = theta_new[:]
  
  return solutions
