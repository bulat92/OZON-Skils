import time

def bubble_sort(array):
    start_time = time.time()
    for i in range(0, len(array) - 1):

        swap = True

        for j in range(len(array) - 1, i, -1):

            if array[j - 1] > array[j]:

                array[j - 1], array[j] = array[j], array[j - 1]
                swap = False
        if swap:
            return (f"Сортировка пузырьком:     размер списка {len(array)} затраченное время {time.time() - start_time}")


array = [5, 3, 9, 23, 6589, 522, 23, 2, 18, 4, 959, 6, 95, 2, 2, 489, 45, 626, 5, 5]

if __name__ == '__main__':
    print(bubble_sort(array))