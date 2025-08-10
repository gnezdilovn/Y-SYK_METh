# Y-SYK_METh
This is a research code developed by Nikolay Gnezdilov to compute the pairing temperature within Migdal-Eliashberg (METh) theory in the Yukawa-SYK model. The results are in arXiv:2505.02894 [cond-mat.str-el] (2025).

Here is a brief description of this repository:

Tc_functions.py -- .py file that contains the necessary functions to compute Tc.

T_arrays.py -- .py file that contains the initial intervals where to look for the Tc solutions for different values of the electron-boson coupling strength.

T_arrays_AD.py -- .py file which is similar to T_arrays.py but is designed for the case when there is no self-consistent account of the self-energy (the bosonic propagator behaves as the Einstein boson).

run_Tc.ipynb -- Jupyter notebook that looks for the Tc solution and checks for convergence.

plot_Tc.ipynb -- Jupyter notebook that plots the data.
