# Supplementary Code for "Optimal Switching Strategies for Navigation in Stochastic Settings"

This repository contains the code to reproduce the numerical simulations presented in the paper and supplementary material. The code is organized into different Python files and notebooks, each corresponding to the reproduction of different figures and results from the paper.

## File Descriptions

### numerical_integration.py
- **Functionality**: Numerically integrates the optimal control equations using an explicit Euler scheme.
- **Outputs**: 
  - `boundary_m_0.01.txt` - Contains the optimal activation angle as a function of time for the negative boundary.
  - `boundary_p_0.01.txt` - Contains the optimal activation angle as a function of time for the positive boundary.

### trajectories_fig1.ipynb
- **Functionality**: Produces the sample trajectories presented in Fig. 2a of the main text.

### simulations.ipynb
- **Functionality**: Verifies the theoretical formula for the maximal speed of the standard random walk model via Langevin numerical simulations.

### execution_error.ipynb
- **Functionality**: Verifies the theoretical formula for the maximal speed in the presence of execution errors via Langevin numerical simulations.

### measurement_error.ipynb
- **Functionality**: Verifies the theoretical formula for the maximal speed in the presence of measurement errors via Langevin numerical simulations.

### partial_observations.ipynb
- **Functionality**: Verifies the theoretical formula for the maximal speed in the presence of partial observability via Langevin numerical simulations.

### first_passage.ipynb
- **Functionality**: Verifies the theoretical formula for the distribution of times between reorientations via Langevin numerical simulations.

---

Each notebook and script is designed to run independently. Please refer to the individual notebooks for detailed instructions and explanations of the numerical methods used.

