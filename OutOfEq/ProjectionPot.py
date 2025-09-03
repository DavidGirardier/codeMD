import numpy as np
import matplotlib.pyplot as plt
from pot import DW10



def free_energy_projection(
    q_array,
    pot_func,
    beta=1.0,             # = 1/(k_B T) in reduced units
    x_min=-5.0,
    x_max=5.0,
    nx=501
):
    """
    Compute F(q) = -1/beta ln[ ∫ exp(-beta U(x, q-2x)) dx ] + const
    by discretizing x from x_min to x_max.

    Parameters
    ----------
    q_array : 1D array
        Array of q-values where you want F(q).
    pot_func : callable
        Function pot_func(x, y) -> float, the 2D potential U(x,y).
    beta : float
        1/(k_B T). If T=1 in reduced units, set beta=1.
    x_min, x_max : float
        Boundaries for the numerical integration in x.
    nx : int
        Number of integration points in x.

    Returns
    -------
    F_array : 1D array
        Same shape as q_array, the resulting free energies, 
        shifted so min(F)=0.
    """

    # 1) Build the x-grid
    x_vals = np.linspace(x_min, x_max, nx)
    dx = x_vals[1] - x_vals[0]

    F_list = []

    for q in q_array:
        # 2) Evaluate U for y = q - 2x
        #    integrand = exp( -beta * U(x, q-2x) )
        #    We'll sum up over x and multiply by dx to approximate the integral.
        exponent_sum = 0.0
        for x in x_vals:
            y = 2.*q - x
            _,_,U_xy = pot_func(x, y)
            exponent_sum += np.exp(-beta * U_xy)

        Z_q = exponent_sum * dx  # approximate integral
        F_q = - (1.0/beta) * np.log(Z_q)
        F_list.append(F_q)

    # Convert to array
    F_array = np.array(F_list)
    # Shift so that the global minimum is zero
    F_array -= F_array.min()
    return F_array

# ---------------------------------------------
# Example usage:
if __name__ == "__main__":

    # We'll define temperature so that beta = 1/(k_B*T). 
    # In dimensionless units with k_B=1, set T=1 => beta=1.
    beta = 1.0

    # We'll pick a range of q-values
    q_vals = np.linspace(-2.0, 2.0, 201)

    # Compute F(q) for the example potential pot_2d
    F_vals = free_energy_projection(
        q_array=q_vals,
        pot_func=DW10,   # use the example U(x,y)=x^2 + y^2
        beta=beta,
        x_min=-3.0,
        x_max=3.0,
        nx=501
    )

    # Plot
    np.savetxt('F_q', np.c_[q_vals,F_vals])
    plt.plot(q_vals, F_vals, '-b')
    plt.xlabel(r"$q$")
    plt.ylabel(r"$F(q)$ (shifted)")
    plt.title("Free energy projected onto q = 2x + y = const.")
    plt.grid(True)
    plt.show()
