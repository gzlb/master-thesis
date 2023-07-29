import fire 
import itertools
from experiments.bsm_gan import main


def calibration():
    # Define the hyperparameter search space
    hyperparameters = {
        'generator_lr': [2e-4],
        'discriminator_lr': [5e-4, 1e-3],
        'steps' : [1000],
        'init_mult1': [0.8, 1, 1.3, 1.5, 1.7],
        'init_mult2': [0.1,0.3,0.5],
    }

    # Perform grid search
    best_loss = float('inf')
    best_params = None

    # Generate all combinations of hyperparameters
    param_combinations = list(itertools.product(*hyperparameters.values()))

    for params in param_combinations:
        param_dict = dict(zip(hyperparameters.keys(), params))

        # Run training with the current set of hyperparameters
        loss = abs(main(**param_dict))

        # Check if current loss is the best so far
        if loss < best_loss:
            best_loss = loss
            best_params = param_dict

    print("Best parameters:", best_params)
    print("Best loss:", best_loss)

if __name__ == '__main__':
    fire.Fire(calibration)