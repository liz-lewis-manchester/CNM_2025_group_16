import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




#### Read + Interpolate initial conditions

def read_and_interpolate_initial_conditions(
    csv_path,
    x_grid,
    distance_col="Distance (m)",
    concentration_col="Concentration (µg/m_ )",
    encoding="latin1"
):
    """
    Read initial_conditions.csv and interpolate onto model grid x_grid.
    Returns: C0 on the grid (nx,)
    """
    df = pd.read_csv(csv_path, encoding=encoding)

    S = df[distance_col].values
    C_meas = df[concentration_col].values

    # interpolate measurements to grid
    C0 = np.interp(x_grid, S, C_meas)
    return C0


###Plot: single profile

def plot_profile(x, C, title="Concentration Profile", save_path=None, show=True):
    plt.figure(figsize=(8, 5))
    plt.plot(x, C, linewidth=2)
    plt.xlabel("Distance x (m)")
    plt.ylabel("Concentration C (µg/m³)")
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()

    if save_path is not None:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=300)

    if show:
        plt.show()
    else:
        plt.close()




#    a graph for each time step (distance vs concentration)

def plot_profiles_each_timestep(x, t, C_all, save_dir=None, show=False, every=1):
    """
    x: 1D array (nx,)
    t: 1D array (nt,)
    C_all: 2D array (nt, nx)
    save_dir: folder to save each timestep plot (optional)
    show: show each plot on screen (False recommended if saving)
    every: plot every N timesteps (e.g., every=5)
    """
    x = np.asarray(x)
    t = np.asarray(t)
    C_all = np.asarray(C_all)

    if C_all.shape != (len(t), len(x)):
        raise ValueError(
            f"C_all shape must be (nt, nx)=({len(t)}, {len(x)}), got {C_all.shape}"
        )

    if save_dir is not None:
        os.makedirs(save_dir, exist_ok=True)

    for n in range(0, len(t), every):
        title = f"Concentration Profile at t = {t[n]:g} s"
        save_path = None
        if save_dir is not None:
            save_path = os.path.join(save_dir, f"profile_t{int(round(t[n])):04d}s.png")

        plot_profile(
            x, C_all[n],
            title=title,
            save_path=save_path,
            show=show
        )


# ## Heatmap (C(t,x))

def plot_heatmap_xt(x, t, C_all, save_path=None, show=True):
    """
    Plot C(t,x) heatmap. C_all must be shape (nt, nx).
    """
    x = np.asarray(x)
    t = np.asarray(t)
    C_all = np.asarray(C_all)

    if C_all.shape != (len(t), len(x)):
        raise ValueError(
            f"Shape of C_all should be (len(t), len(x)) = ({len(t)}, {len(x)}), got {C_all.shape}"
        )

    plt.figure(figsize=(10, 6))
    plt.imshow(
        C_all,
        aspect="auto",
        origin="lower",
        extent=[x.min(), x.max(), t.min(), t.max()]
    )
    plt.colorbar(label="C (µg/m³)")
    plt.xlabel("Distance x (m)")
    plt.ylabel("Time t (s)")
    plt.title("Concentration heatmap C(t, x)")
    plt.tight_layout()

    if save_path is not None:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=300)

    if show:
        plt.show()
    else:
        plt.close()


#
def run_simple_advection(C0, U, x, t):
    """
    Simple upwind scheme for: dC/dt + U dC/dx = 0
    Returns C_all with shape (nt, nx)
    """
    dx = x[1] - x[0]
    dt = t[1] - t[0]

    # Stability check
    cfl = U * dt / dx
    if cfl > 1.0:
        print(f"WARNING: CFL = {cfl:.2f} > 1.0, scheme may be unstable. Consider smaller dt or larger dx.")

    nt = len(t)
    nx = len(x)
    C_all = np.zeros((nt, nx))
    C_all[0] = C0.copy()

    C = C0.copy()

    for n in range(1, nt):
        C_new = C.copy()
        # upwind (for U > 0)
        for i in range(1, nx):
            C_new[i] = C[i] - cfl * (C[i] - C[i - 1])

        # boundary condition at x=0 (keep as given/fixed)
        C_new[0] = C[0]

        C = C_new
        C_all[n] = C

    return C_all


# #Main one script workflow

def get_float_input(prompt, default): ##For user input
    
    user_input = input(f"{prompt} [default = {default}]: ")
    if user_input.strip() == "":
        return default
    return float(user_input)

if __name__ == "__main__":
    print("Please enter model parameters (press Enter to use default values):")

    L  = get_float_input("Total river length L (m)", 20.0)
    dx = get_float_input("Spatial resolution dx (m)", 0.2)
    T  = get_float_input("Total simulation time T (s)", 300.0)
    dt = get_float_input("Time step dt (s)", 10.0)
    U  = get_float_input("Flow velocity U (m/s)", 0.1)

    # grids
    x = np.arange(0, L + dx, dx)
    t = np.arange(0, T + dt, dt)

    # read + interpolate initial conditions
    csv_path = "initial_conditions.csv"   # put the file in fold
    C0 = read_and_interpolate_initial_conditions(csv_path, x)

    print("x shape:", x.shape)
    print("C0 shape:", C0.shape)

    # plot initial condition (one profile)
    plot_profile(x, C0, title="Initial pollutant concentration", save_path="results/figures/initial_C0.png", show=True)

    # --- run model
    C_all = run_simple_advection(C0, U, x, t)

    # profile graph for each time step
    plot_profiles_each_timestep(
        x, t, C_all,
        save_dir="results/figures/profiles_each_timestep",
        show=True,   # change to control them displayed or not
        every=1       # every=5 to reduce number of figures
    )

    # ---create a heatmap summary
    plot_heatmap_xt(x, t, C_all, save_path="results/figures/heatmap.png", show=True)
