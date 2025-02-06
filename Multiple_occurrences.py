import sys

def calculate_index_difference(n, arr):
    first_occurrence = {}
    last_occurrence = {}
    
    # Identify first and last occurrence of each element
    for i, num in enumerate(arr):
        if num not in first_occurrence:
            first_occurrence[num] = i  # Store first occurrence
        last_occurrence[num] = i  # Always update last occurrence

    # Calculate sum of absolute differences
    total_sum = sum(abs(last_occurrence[num] - first_occurrence[num]) for num in first_occurrence)
    
    return total_sum

# Fast input handling
input = sys.stdin.read
data = input().split()

# Processing input
T = int(data[0])
index = 1
results = []

for _ in range(T):
    N = int(data[index])  # Number of elements
    A = list(map(int, data[index + 1 : index + 1 + N]))  # Read array
    index += 1 + N  # Move to next test case
    
    # Compute and store result
    results.append(str(calculate_index_difference(N, A)))

# Fast output
sys.stdout.write("\n".join(results) + "\n")
