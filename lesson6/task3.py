def calculate_mean(*numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

calculate_mean(1, 2, 3, 4, 5)

