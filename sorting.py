import random


def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]


def selection_sort(values):
    n = 0
    while n < len(values):
        min_index = n
        min_value = values[min_index]
        for i in range(n + 1, len(values)):
            if values[i] < min_value:
                min_index = i
                min_value = values[i]
        values[n], values[min_index] = values[min_index], values[n]
        n += 1
    print(values)


if __name__ == "__main__":
    values = random_numbers(10)  # 10 čísel v rozsahu 0–100
    print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]

    small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20
    print(small)

    selection_sort([42, 7, 91, 15, 63, 8, 57, 73, 2, 100])