def bubble_sort(collection) -> None:
    for i in range(len(collection) - 1):
        for j in range(i + 1, len(collection)):
            if collection[i] > collection[j]:
                collection[i], collection[j] = collection[j], collection[i]


def bubble_sort_descending(collection) -> None:
    for i in range(len(collection) - 1):
        for j in range(i + 1, len(collection)):
            if collection[i] < collection[j]:
                collection[i], collection[j] = collection[j], collection[i]


def selection_sort(collection) -> None:
    for i in range(len(collection) - 1):
        min_index = i
        for j in range(i + 1, len(collection)):
            if collection[j] < collection[min_index]:
                min_index = j
        collection[i], collection[min_index] = collection[min_index], collection[i]


def selection_sort_descending(collection) -> None:
    for i in range(len(collection) - 1):
        max_index = i
        for j in range(i + 1, len(collection)):
            if collection[j] > collection[max_index]:
                max_index = j
        collection[i], collection[max_index] = collection[max_index], collection[i]


def insertion_sort(collection) -> None:
    n = len(collection)
    for i in range(1, n):
        key = collection[i]
        j = i - 1
        while (j >= 0) & (collection[j] > key):
            collection[j + 1] = collection[j]
            j = j - 1
        collection[j + 1] = key


def insertion_sort_descending(collection) -> None:
    n = len(collection)
    for i in range(1, n):
        key = collection[i]
        j = i - 1
        while (j >= 0) & (collection[j] < key):
            collection[j + 1] = collection[j]
            j = j - 1
        collection[j + 1] = key


collection_1 = [6, 1, 7, 3, 4, 9, 2, 5, 8, 0]
collection_2 = [8, 5, 4, 2, 1, 7, 9, 6, 0, 3]
collection_3 = [3, 4, 0, 7, 1, 5, 2, 8, 9, 6]
collection_4 = [3, 4, 1, 2, 5, 0, 9, 8, 6, 7]
collection_5 = [3, 5, 8, 7, 1, 6, 9, 4, 0, 2]
collection_6 = [0, 7, 9, 4, 8, 6, 5, 3, 2, 1]


bubble_sort(collection_1)
print(collection_1)

bubble_sort_descending(collection_2)
print(collection_2)

selection_sort(collection_3)
print(collection_3)

selection_sort_descending(collection_4)
print(collection_4)

insertion_sort(collection_5)
print(collection_5)

insertion_sort_descending(collection_6)
print(collection_6)
