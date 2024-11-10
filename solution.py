import statistics

def calculate_statistics(numbers):
    mean = statistics.mean(numbers)
    median = statistics.median(numbers)
    mode = statistics.mode(numbers)

    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")

numbers = [1, 2, 3, 4, 4, 5, 6]
calculate_statistics(numbers)
