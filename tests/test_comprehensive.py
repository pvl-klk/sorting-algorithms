import pytest
import random
from collections import Counter

from src.heap_sort import heap_sort
from src.quick_sort import quick_sort
from src.bubble_sort import bubble_sort
from src.merge_sort import merge_sort

SORTING_FUNCTIONS = [heap_sort, quick_sort, bubble_sort, merge_sort]


@pytest.fixture
def unsorted_lists() -> list[list]:
    sizes = [5, 10, 15, 20, 30, 50]
    lists = []
    for size in sizes:
        array = []
        for _ in range(size):
            array.append(random.randint(-100, 100))
        lists.append(array)

    return lists


@pytest.mark.parametrize("sorting_function", SORTING_FUNCTIONS)
def test_orderliness(sorting_function, unsorted_lists) -> None:
    for unsorted_list in unsorted_lists:
        sorted_array = sorting_function(unsorted_list)
        for index in range(1, len(sorted_array)):
            assert sorted_array[index] >= sorted_array[index - 1]


@pytest.mark.parametrize("sorting_function", SORTING_FUNCTIONS)
def test_elements_sameness(sorting_function, unsorted_lists) -> None:
    for unsorted_list in unsorted_lists:
        sorted_list = sorting_function(unsorted_list)
        assert Counter(sorted_list) == Counter(unsorted_list)


@pytest.mark.parametrize("sorting_function", SORTING_FUNCTIONS)
def test_idempotency(sorting_function, unsorted_lists):
    for unsorted_list in unsorted_lists:
        first_sort = sorting_function(unsorted_list.copy())
        second_sort = sorting_function(first_sort.copy())

        assert first_sort == second_sort


@pytest.fixture(
    params=[
        [],
        [1],
        [1, 1, 1],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [1, 3, 2, 3, 1],
        [-1, -5, 2, -3, 0],
        [100, -100, 0, 50, -50],
        [1] * 100,
        list(range(100, 0, -1)),
    ]
)
def edge_case_list(request):
    return request.param


@pytest.mark.parametrize("sorting_function", SORTING_FUNCTIONS)
def test_edge_cases(sorting_function, edge_case_list):
    original = edge_case_list.copy()
    sorted_list = sorting_function(edge_case_list)

    assert sorted_list == sorted(original)
