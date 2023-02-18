# Generate a data sequence where the Hamming distance between adjacent bit sequences is constant

import random

# Specify the length of the bit sequence
bit_length = 32

# Specify the number of bit sequences to generate
generate_times = 10

# Specify the desired Hamming distance between adjacent bit sequences
hamming_distance = 30

# Generate a data sequence where the Hamming distance between adjacent bit sequences is constant
def ham(bit_length, generate_times, hamming_distance):
  # Generate an initial bit sequence with random bits
  bitstream = [random.randint(0,1) for _ in range(bit_length)]
  for _ in range(generate_times):

    # Generate the index values for the bits to be flipped
    data_index = [i for i in range(bit_length)]
    for _ in range(hamming_distance):

      # Choose a random index from data_index and flip the bit at that index
      reversal_index = data_index.pop(random.randint(0,len(data_index)-1))
      bitstream[reversal_index] = abs(bitstream[reversal_index] - 1)
    print("".join(map(str,bitstream)))

# Execute the code
if hamming_distance <= bit_length:
  ham(bit_length, generate_times, hamming_distance)
else:
  print("***bit_length must be longer than hamming_distance***")

