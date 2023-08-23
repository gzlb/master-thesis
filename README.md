# master-thesis


This is the code which accompanies my thesis. In this short note, a summary is provided with regards to running the files. 

## Prerequisites

- Python 3.8 or higher

## Getting Started

1. **Clone the Repository**: Start by cloning this repository to your local machine.

   ```bash
   git clone https://github.com/gzlb/master-thesis.git


2. **Navigate to the Project Directory**: Move into the project directory.

   ```bash
   cd your-project

3. **Install Dependencies**

    Utilize Poetry to install project dependencies listed in the `pyproject.toml` file.

    ```bash
    poetry install


## Scripts 

A short overview of each script:

### Calibration
- **bsm_gan:** calibration performed for the Black-Scholes SDE-GAN
- **heston_gan:**  calibration performed for the Heston SDE-GAN

### Experiments: 
The first half of the experiments belong to chapter 7
- **bsm_gan_1:** BSM-GAN without normalization and normal distribution as initial condition, not-mean square stable
- **bsm_gan_mss:** BSM-GAN with normalization and uniform distribution as initial condition, mean square stable
- **bsm_gan_notmss:** BSM-GAN with normalization and uniform distribution as initial condition, not-mean square stable
- **bsm_gan:**  BSM-GAN without normalization and uniform distribution as initial condition, mean square stable
- **bsm_latent:** latent-BSM, with normalization and normal distribution as initial condition, not-mean square stable
- **calibrated_bsm_gan:** BSM-GAN with normalization and uniform distribution as initial condition, mean square stable, here calibration is applied in the main function
- **heston_gan:** Heston-GAN, with normalization and uniform distribution as initial condition
- **heston_latent:** latent-Heston with normalization and normal distribution as initial condition
- **calibrated_heston_gan:** BSM-GAN with normalization and uniform distribution as initial condition, here calibration is applied in the main function
The experiments below belong to Appendix B
- **ornstein_uhlenbeck_mod_1:** Ornstein-Uhlenbeck experiment 1
- **ornstein_uhlenbeck_mod_2:** Ornstein-Uhlenbeck experiment 2
- **ornstein_uhlenbeck_mod_3:** Ornstein-Uhlenbeck experiment 3
- **ornstein_uhlenbeck_mod_4:** Ornstein-Uhlenbeck experiment 4
- **ornstein_uhlenbeck_div:** Ornstein-Uhlenbeck experiment 5
- **ornstein_uhlenbeck** Ornstein-Uhlenbeck experiment, very first experiment of Appendix B. This is a replication of Kidger's results 
- **sde_lorentzk** Lorentz-SDE experiment, first experiment of Appendix B.2 This is a replication of Kidger's results 
