import numpy as np


def calculate(numbers):
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(numbers).reshape(3, 3)

    mean = [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean().tolist()]
    variance = [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var().tolist()]
    std_dev = [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std().tolist()]
    max_val = [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max().tolist()]
    min_val = [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min().tolist()]
    sum_val = [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum().tolist()]

    return {
        'mean': mean,
        'variance': variance,
        'standard deviation': std_dev,
        'max': max_val,
        'min': min_val,
        'sum': sum_val
    }


if __name__ == "__main__":
    try:
        user_input = input("Enter 9 numbers separated by spaces: ")

        numbers = list(map(int, user_input.split()))
        result = calculate(numbers)
        print(result)

    except ValueError as e:
        print(e)
