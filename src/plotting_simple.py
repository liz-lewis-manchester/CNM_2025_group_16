import numpy as np
import matplotlib.pyplot as plt

def plot_heatmap_xt(x, t, C, save_path=None):
  #plot C(t,x) heatmap
  #x is nx, t is nt, C is matrix of nt,nx
  #save_path is used for graph saving
  x = np.array(x)
  t = np.array(t)
  C = np.array(C)

  if C.shape ! = (len(t),len(x)):
    raise ValueError("Shape of C should be (len(t), len(x)) or '(nt,nx)', try again")  #for external user

  plt.figure(figsize=(8, 5))   #adjust size of graph

  plt.imshow(
    C,
    aspect="auto"
    origin="lower"
    extent=[x.min(), x.max(), t.min(), t.max()]
  )

  plt.colorbar(label = "C(µg/m³)")
  plt.xlabel("Distance x (m)")         # x 
  plt.ylabel("Time t (s)")             # y
  plt.title("Concentration heatmap C(t, x)")  #title

  plt.tight_layout()
"""
  if save_path is not None:
    plt.savefig(save_path,dpi=300)
"""
plt.show()
