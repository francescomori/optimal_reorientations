# Supplementary code for the article "Optimal switching strategies for navigation in stochastic settings"

The code allows to reproduce the numerical simulations presented in the paper and supplemental material. The code is divided into different python files notebooks, that correspond to the reproduction fo different figures.

numerical_integration.py allows to numerically integrate the optimal control equations using an euler explicit scheme. It outputs the optimal activation angle as a function of time into the two files boundary_m_0.01.txt and boundary_p_0.01.txt (for the negative and positive boundaries).

trajectories_fig1.ipynb produces the sample trajectories presented in Fig. 2a of the main text.

simulations.ipynb verifies, via Langevin numerical simulations, the theoretical formula for the maximal speed of the standard random walk model.

execution_error.ipynb verifies, via Langevin numerical simulations, the theoretical formula for the maximal speed in the presence of execution errors.

measurement_error.ipynb verifies, via Langevin numerical simulations, the theoretical formula for the maximal speed in the presence of measurements errors.

partial_observations.ipynb verifies, via Langevin numerical simulations, the theoretical formula for the maximal speed in the presence of partial observability.

first_passage.ipynb verifies, via Langevin numerical simulations, the theoretical formula for the distribution of the times between reorientations.



