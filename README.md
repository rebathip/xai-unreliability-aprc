# xai-unreliability-aprc

The Python script "analysis_prob_diffs.py" calculates Kendall's Tau correlation coefficients for a set of probability files.

## Usage
1. Save the probability files in the `results` directory.
2. Run the script to compute the Kendall's Tau for each file.
3. The script will print the mean and standard deviation of the Kendall's Tau for each label, as well as the overall mean and standard deviation.

## Requirements
- Python 3
- NumPy
- SciPy

## How it Works
The script loops over the files in the `results` directory and loads the probabilities stored in each file. It then computes the Kendall's Tau correlation coefficient between the probabilities for each triplet of images in the file. The final output includes the mean and standard deviation of the Kendall's Tau for each label and the overall mean and standard deviation.
