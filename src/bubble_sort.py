def bubble_sort(array: list) -> list:
    for index_1 in range(len(array)):
        for index_2 in range(index_1 + 1, len(array)):
            if array[index_1] > array[index_2]:
                array[index_1], array[index_2] = array[index_2], array[index_1]

    return array
