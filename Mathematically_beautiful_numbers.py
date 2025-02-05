def is_mathematically_beautiful(x, k):
    while x > 0:
        if x % k > 1:  # Coefficients must be 0 or 1
            return "NO"
        x //= k
    return "YES"

# Read number of test cases
T = int(input().strip())

for _ in range(T):
    x, k = map(int, input().split())
    print(is_mathematically_beautiful(x, k))
