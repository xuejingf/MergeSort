def ASSIGNMENT(new_list, i, old_list, j):
    new_list[i] = old_list[j]

import matplotlib.pyplot as plt

def plot_list(list_to_plot):
    plt.bar(range(len(list_to_plot)), list_to_plot)
    plt.show(block=False)
    plt.pause(5)
    plt.clf() # Das aktuelle Bild löschen

def mergeSort(list_to_sort_by_merge):
    if (
        len(list_to_sort_by_merge) > 1
        and not len(list_to_sort_by_merge) < 1
        and len(list_to_sort_by_merge) != 0
    ):
        mid = len(list_to_sort_by_merge) // 2
        left = list_to_sort_by_merge[:mid]
        right = list_to_sort_by_merge[mid:]

        mergeSort(left)
        mergeSort(right)

        l = 0
        r = 0
        i = 0

        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                ASSIGNMENT(new_list=list_to_sort_by_merge, i=i, old_list=left, j=l)
                l += 1
            else:
                ASSIGNMENT(new_list=list_to_sort_by_merge, i=i, old_list=right, j=r)
                r += 1
            i += 1

        while l < len(left):
            list_to_sort_by_merge[i] = left[l]
            l += 1
            i += 1

        while r < len(right):
            list_to_sort_by_merge[i] = right[r]
            r += 1
            i += 1
    

my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
plot_list(my_list)
mergeSort(my_list)
plot_list(my_list)


