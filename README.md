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
- **bsm_gan.py:** calibration performed for the Black-Scholes SDE-GAN
- **heston_gan.py:**  calibration performed for the Heston SDE-GAN

### Experiments
- **bsm_gan_1:** BSM-GAN without normalization and normal distribution as initial condition, not-mean square stable
- **bsm_gan_mss:** BSM-GAN with normalization and uniform distribution as initial condition, mean square stable
- **bsm_gan_notmss:** BSM-GAN with normalization and uniform distribution as initial condition, not-mean square stable
- **bsm_gan:**  BSM-GAN without normalization and uniform distribution as initial condition, mean square stable
- **bsm_latent:** latent-BSM 
- **calibrated_bsm_gan:** BSM-GAN with normalization and uniform distribution as initial condition, mean square stable, here calibration is applied in the main function
- **heston_gan:** Heston-GAN, with normalization and uniform distribution as initial condition
- **heston_latent:** latent-Heston
- **calibrated_heston_gan:** BSM-GAN with normalization and uniform distribution as initial condition, here calibration is applied in the main function.
- **ornstein_uhlenbeck_mod_1:** Description of script 8.
- **ornstein_uhlenbeck_mod_2:** Description of script 9.
- **ornstein_uhlenbeck_mod_3:** Description of script 10.
- **ornstein_uhlenbeck_mod_4:** Description of script 7.
- **ornstein_uhlenbeck_div:** Description of script 8.
- **ornstein_uhlenbeck** Description of script 9.
