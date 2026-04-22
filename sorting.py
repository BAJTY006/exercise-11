import random
# import matplotlib.pyplot as plt


def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]


def selection_sort(values_original):
    values = values_original.copy()
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
    return values


values = [42, 7, 100, 91, 15, 63, 8, 57, 73, 2]
def bubble_sort(values_original):
    plt.ion()
    plt.show()
    values = values_original.copy()
    n = 1
    while n < len(values):
        for i in range(len(values) - n):
            if values[i] > values[i + 1]:
                values[i], values[i + 1] = values[i + 1], values[i]
                # index_highlight1 = i
                # index_highlight2 = i + 1
                # colors = ["steelblue"] * len(values)
                # colors[index_highlight1] = "tomato"
                # colors[index_highlight2] = "tomato"
                # plt.clf()
                # plt.bar(range(len(values)), values, color=colors)
                # plt.title("Bubble Sort")
                # plt.pause(0.1)
        n += 1
    plt.ioff()
    plt.show()
    return values




if __name__ == "__main__":
    seznam = random_numbers(20)  # 10 čísel v rozsahu 0–100
    # print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]
    #
    # small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20
    # print(small)
    #
    # seznam = [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]
    # print(selection_sort(seznam))
    # print(seznam)

    print(bubble_sort(seznam))
    print(seznam)