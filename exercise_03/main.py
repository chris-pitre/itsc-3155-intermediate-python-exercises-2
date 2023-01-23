# Chris Pitre
# Intermediate Python Exercises 2
# Exercise 3

import numpy as np

rng = np.random.default_rng()
float_array = rng.random(10)

print("Random numbers: ")
print(float_array)

mean = np.mean(float_array)
median = np.median(float_array)
std_dev = np.std(float_array)

print(f"Mean : {mean}, Median: {median}, Standard Deviation: {std_dev}")