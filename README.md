# xai-unreliability-aprc

This repository contains two Python scripts:
1. `calculate_prob_diffs.py`: Generates probability values for images using a pre-trained InceptionV3 model.
2. `metrics_calculator.py`: Calculates proposed metrics i.e. ARPPD and APRC for a set of probability files generated by the first script.

## Usage

### Step 1: Calculate probabilities
1. Save the images to be processed in the `cifar10_test/` directory. Use other datasets as needed.
2. Run `calculate_prob_diffs.py` to generate probability values for the images using the InceptionV3 model. Use other models with their appropriate preprocessing function and image size etc to run for other models.
3. The script will save the probabilities in `.pkl` files in the working directory.

### Step 2: Calculate APRC
1. Save the probability files generated in Step 1 in the `results` directory.
2. Run `metrics_calculator.py` to compute the ARPPD and APRC for each probability file.
3. The script will print the mean and standard deviation of the Kendall's Tau for each label, as well as the overall mean and standard deviation.

## Requirements
- Python 3
- TensorFlow
- Keras
- NumPy
- SciPy
- scikit-image
- OpenCV

## How it Works
- `calculate_prob_diffs.py` uses the pre-trained InceptionV3 model to predict the probability values for each image. The images are perturbed using Gaussian blur and the probabilities are stored in a `.pkl` file.
- `metrics_calculator.py` reads the `.pkl` files generated in the previous step, computes the ARPPD and APRC between the probabilities for each triplet of probability differences(corresponding to each sigma of Gaussian Blur), and outputs the mean and standard deviation of the metrics for each label and overall.
