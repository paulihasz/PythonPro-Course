def list_analysis(numbers: list[int]) -> tuple[int]:
    if not numbers:
        return (0, 0, 0)
    return f'suma = {sum(numbers)}, minimum = {min(numbers)}, maksimum = {max(numbers)}'

list_analysis([3, 1, 4, 1, 5, 9])
list_analysis([])


