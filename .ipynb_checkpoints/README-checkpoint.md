# Supplementary Code for "Optimal Switching Strategies for Navigation in Stochastic Settings"

This repository contains the code to reproduce the numerical simulations presented in the paper and supplementary material. The code is organized into different Python files and notebooks, each corresponding to the reproduction of different figures and results from the paper.

## File Descriptions


### supp_material.pdf
Presents supplental analytical derivations and outlines the details of the numerical simulations.

### numerical_integration.py
- **Functionality**: Numerically integrates the optimal control equations using an explicit Euler scheme.
- **Outputs**: 
  - `boundary_m_0.01.txt` - Contains the optimal activation angle as a function of time for the negative boundary.
  - `boundary_p_0.01.txt` - Contains the optimal activation angle as a function of time for the positive boundary.

### trajectories_fig1.ipynb
- **Functionality**: Reads the boundary files `boundary_m_0.01.txt` and `boundary_p_0.01.txt` and produces sample trajectories.
- **Outputs**: Fig. 2a of the main text
  
### simulations.ipynb
- **Functionality**: Verifies the theoretical formula for the maximal speed of the standard random walk model via Langevin numerical simulations.
- **Outputs**: Fig. 2b and 2c of the main text

### first_passage.ipynb
- **Functionality**: Verifies the theoretical formula for the distribution of times between reorientations via Langevin numerical simulations.
-  **Outputs**: Fig. 3 of the main text


### execution_error.ipynb
- **Functionality**: Verifies the theoretical formula for the maximal speed in the presence of execution errors via Langevin numerical simulations.
- **Outputs**: Fig. 4a of the main text and Fig. 1 of the supplementary material.
  
### measurement_error.ipynb
- **Functionality**: Verifies the theoretical formula for the maximal speed in the presence of measurement errors via Langevin numerical simulations.
-  **Outputs**: Fig. 4b of the main text

### partial_observations.ipynb
- **Functionality**: Verifies the theoretical formula for the maximal speed in the presence of partial observability via Langevin numerical simulations.
- **Outputs**: Fig. 4c of the main text

### partial_observations.ipynb
- **Functionality**: Compares the optimal strategy with the best Poissonian strategy.
- **Outputs**: Fig. 2 of the supplementary material

### trajectories.ipynb
- **Functionality**: Simulates random trajectories of the optimally-controlled process at different noise levels.
- **Outputs**: Fig. 2 of the main text
- 
### non_inst.ipynb
- **Functionality**: For the model with non-instantaneous reorientations, verifies the theoretical formula for the  maximal speed and fraction of time spent in the reorientation phase via Langevin numerical simulations.

---

Each notebook and script is designed to run independently. Please refer to the individual notebooks for detailed instructions and explanations of the numerical methods used.

