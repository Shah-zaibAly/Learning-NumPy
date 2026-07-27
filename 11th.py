import numpy as np

# Random Numbers

rng = np.random.default_rng()

print(rng.random(3))  # returns three random numbers between 0 and 1
print(rng.integers(5, 101))  # 5 is inclusive and 101 is exclusive
print(rng.integers(10, 20, size=5))  # will return 5 random numbers bw 10 and 20
print(rng.integers(50, 90, size=(3,2)))  # will return an [3,2] array of random numbers