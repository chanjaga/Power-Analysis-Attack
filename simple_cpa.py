import itertools
import numpy as np
from tqdm.notebook import tqdm
import matplotlib.pyplot as plt
from scipy.spatial import distance

# Generate all possible plaintexts (i.e., 256 8-bit values)
plaintext = [list(i) for i in itertools.product([0, 1], repeat=8)]

# Generate all possible 8-bit pre-round keys
pre_round_key = [list(i) for i in itertools.product([0, 1], repeat=8)]

# Compute the number of possible pre-round keys (i.e., 256)
pre_round_key_number = len(pre_round_key)

# Compute the number of round keys that will be estimated (i.e., 16)
round_key_number = 16

# Define the number of power traces that will be observed
obs_trace_times = 100

# Define a leakage model that simulates the power consumption of the device during encryption.
def leakage_model(plaintext, pre_round_key):
    # Calculate the Hamming distance between the plaintext and the pre-round key and add some random noise.
    leakage = distance.hamming(pre_round_key, plaintext) + np.random.rand()
    return leakage

# Perform a correlation power analysis to estimate the round keys.
def cpa(pre_round_key, plaintext):
    correlation = []
    result_correlation = []
    for i in tqdm(range(pre_round_key_number)):
        pre_trace = []
        dumy_obs_trace = []
        for j in range(obs_trace_times):
            # Generate the predicted power trace for the current pre-round key and plaintext
            pre_trace.append(leakage_model(pre_round_key[i], plaintext[j%256]))
            # Generate a dummy power trace for a random pre-round key and the same plaintext
            dumy_obs_trace.append(leakage_model(pre_round_key[np.random.randint(100,200)], plaintext[j%256]))

        # Compute the correlation coefficient between the predicted and dummy power traces
        correlation.append(np.corrcoef(pre_trace, dumy_obs_trace))
        # Extract the correlation coefficient value
        result_correlation.append(correlation[i][1][0])

        # Plot the correlation coefficient for each iteration
        plt.plot(result_correlation)
    plt.ylim(0,0.7)
    plt.xlabel("key_candidate")
    plt.ylabel("correlation")
    plt.show()

    # Identify the pre-round key with the highest correlation coefficient (i.e., the most likely round key)
    round_key_index = np.argmax(result_correlation)
    round_key = pre_round_key[round_key_index]
    # Convert the round key from binary to hexadecimal
    result_bin = "".join(map(str,round_key))
    hex_cal = 0
    for j in range(len(round_key)):
        hex_cal += round_key[j]*2**(len(round_key)-1-j)
    result_hex = format(hex_cal, 'x')

    # Pad the result with a leading zero if necessary (to ensure that it is two characters long)
    if len(result_hex) == 1:
        result_hex += "0"

    # Print the estimated round key in binary and hexadecimal formats
    print(f"Round key (binary): {result_bin}")
    print(f"Round key (hexadecimal): {result_hex}\n")
    return result_hex

# Estimate each of the 16 round keys using CPA
round_key_list = []
for i in range(round_key_number):
    print(f"[Estimating round key {i+1}]")
    round_key_list.append(cpa(pre_round_key, plaintext))
print(f"Encryption key: {''.join(round_key_list)}")
