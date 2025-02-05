import sys

def compute_sum(N):
    return N * (N + 1)

# Fast input reading
input = sys.stdin.read
data = input().split()

# Number of test cases
T = int(data[0])
results = []

for i in range(1, T + 1):
    N = int(data[i])
    results.append(str(compute_sum(N)))

# Print all results efficiently
sys.stdout.write("\n".join(results) + "\n")
