def heap_sort(array: list) -> list:
    length = len(array)

    for index in range(length // 2 - 1, -1, -1):
        heapify(array, length, index)

    for index in range(length - 1, 0, -1):
        array[0], array[index] = array[index], array[0]
        heapify(array, index, 0)

    return array


def heapify(array: list, length: int, index: int) -> None:
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < length and array[left] > array[largest]:
        largest = left

    if right < length and array[right] > array[largest]:
        largest = right

    if largest != index:
        array[index], array[largest] = array[largest], array[index]
        heapify(array, length, largest)
