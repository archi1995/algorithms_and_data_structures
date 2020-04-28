def swap(list_, index):
    list_[index], list_[index + 1] = list_[index + 1], list_[index]


def is_unordered(list_, index):
    return list_[index] > list_[index + 1]


def bubble_sort(unsorted):
    sorting = True
    for iteration in range(len(unsorted)):
        lasted_range = range(len(unsorted) - iteration - 1)
        for elem in lasted_range:
            if is_unordered(unsorted, elem):
                swap(unsorted, elem)
            else:
                sorting = False
        if not sorting:
            break


if __name__ == '__main__':
    unsorted = [5, 4, 3, 2, 1]
    bubble_sort(unsorted)
    print(unsorted)
