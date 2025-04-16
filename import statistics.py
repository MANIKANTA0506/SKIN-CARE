import statistics
# Dynamic input: Accept dataset from the user
data = list(map(float, input("Enter the dataset values separated by spaces: ").split()))
# Mean
mean = sum(data) / len(data)
print("\nMean (manual):", mean)
print("Mean (library):", statistics.mean(data))
# Median
sorted_data = sorted(data)
n = len(data)
median = (sorted_data[n // 2] + sorted_data[(n - 1) // 2]) / 2 if n % 2 == 0 else sorted_data[n // 2]
print("\nMedian (manual):", median)
print("Median (library):", statistics.median(data))
# Mode
mode = statistics.mode(data)
print("\nMode (library):", mode)
# Variance
mean_square_diff = sum((x - mean) ** 2 for x in data) / len(data)
print("\nVariance (manual):", mean_square_diff)
print("Variance (library):", statistics.variance(data))
# Standard Deviation
std_dev = mean_square_diff ** 0.5
print("\nStandard Deviation (manual):", std_dev)
print("Standard Deviation (library):", statistics.stdev(data))