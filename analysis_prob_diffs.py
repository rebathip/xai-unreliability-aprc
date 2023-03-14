import os
import pickle
import math
import numpy as np
from scipy import stats


# Define a function to extract the label name from a file name
def extract_label(file_name):
    label_tokens = file_name.split('_')
    return '_'.join(label_tokens[0:2])


# Define the directory where the results files are stored
results_dir = 'results/'

# Initialize some variables to store the results
labels_list = []
ktaus_list = []
means = []
num_pv_gr = 0
img_count = 0

# Loop over the results files
res_files = os.listdir(results_dir)
for res_file in res_files:
    # Extract the label name from the file name and store it in the list
    res_file_label = extract_label(res_file)
    labels_list.append(res_file_label)

    # Load the probabilities from the results file
    with open(results_dir + res_file, 'rb') as f:
        loaded_probs = pickle.load(f)

    # Loop over the loaded probabilities and compute the Kendall's Tau
    ktaus = []
    for idx in range(0, len(loaded_probs), 3):
        img_name = loaded_probs[idx][-1]
        prob0 = loaded_probs[idx][-2]
        prob0 = prob0.astype('float64')
        sigma = loaded_probs[idx][-3]
        probs1 = loaded_probs[idx][:-3].astype('float64')
        probs2 = loaded_probs[idx + 1][:-3].astype('float64')
        probs3 = loaded_probs[idx + 2][:-3].astype('float64')

        probs_diff1 = prob0 - probs1
        probs_diff2 = prob0 - probs2
        probs_diff3 = prob0 - probs3

        ktau1 = stats.kendalltau(probs_diff1, probs_diff2)
        ktau2 = stats.kendalltau(probs_diff2, probs_diff3)
        ktau3 = stats.kendalltau(probs_diff1, probs_diff3)

        for ktau in [ktau1, ktau2, ktau3]:
            if math.isnan(ktau.pvalue) == False:
                if ktau.pvalue > 0.05:
                    num_pv_gr += 1
                else:
                    if (probs_diff1 == 0).all() or (probs_diff2 == 0).all():
                        ktaus.append(1)
                    else:
                        ktaus.append(ktau.correlation)

    # Store the computed Kendall's Tau values in the list
    ktaus = np.array(ktaus)
    ktaus_list.append(ktaus)

    # Compute and store the mean Kendall's Tau for this label
    mean_ktau = round(np.mean(ktaus), 4)
    means.append(mean_ktau)

    # Print the mean and standard deviation of the Kendall's Tau for this label
    print(f'{res_file_label} Mean: {mean_ktau} Stdev: {round(np.std(ktaus), 4)}')

# Compute the overall mean and standard deviation of the Kendall's Tau
all_ktaus = np.concatenate(ktaus_list)
overall_mean = round(np.mean(all_ktaus), 4)
overall_stdev = round(np.std(all_ktaus), 4)
print(f'Overall Mean: {overall_mean} Stdev: {overall_stdev}')