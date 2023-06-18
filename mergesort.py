def assignment(new_list, i, old_list, j):
    new_list[i] = old_list[j]

import matplotlib.pyplot as plt

def plot_list(list_to_plot):
    plt.bar(range(len(list_to_plot)), list_to_plot)
    plt.show(block=False)
    plt.pause(5)
    plt.clf() # Das aktuelle Bild löschen

def merge_sort(list_to_sort):
    if len(list_to_sort) > 1:
        # Aufteilen der Liste in zwei Hälften
        mid = len(list_to_sort) // 2
        left = list_to_sort[:mid]
        right = list_to_sort[mid:]

        # Rekursiver Aufruf von mergeSort für die beiden Hälften
        merge_sort(left)
        merge_sort(right)

        # Zusammenführen der sortierten Hälften
        l = 0
        r = 0
        i = 0

        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                # Verwendung der Funktion 'zuweisung' für die Zuweisung der Werte
                assignment(list_to_sort, i, left, l)
                l += 1
            else:
                assignment(list_to_sort, i, right, r)
                r += 1
            i += 1
        # Hinzufügen der übrig gebliebenen Elemente von linke_haelfte
        while l < len(left):
            list_to_sort[i] = left[l]
            l += 1
            i += 1
        # Hinzufügen der übrig gebliebenen Elemente von rechte_haelfte
        while r < len(right):
            list_to_sort[i] = right[r]
            r += 1
            i += 1
    

my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()


# Aufruf von mergeSort, um die Liste zu sortieren
merge_sort(my_list)

x = range(len(my_list))
plt.plot(x, my_list)
plt.show()
