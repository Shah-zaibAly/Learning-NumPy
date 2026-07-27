import numpy as np

# Comparison Operator

Score = np.array([43, 56, 77, 98, 21, 52, 65, 100])

print(Score == 100)  # ture for which is correct others false
print(Score >= 60)

Score[Score < 50] = 0
print(Score)