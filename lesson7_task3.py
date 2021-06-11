import random, time, copy
from lesson7_task2 import bubble_sort as bubble_sort
from lesson7_task4 import heap_sort as heap_sort

def selection_sort(input_list):
    start_time = time.time() # время старта функции
    for i in range(len(input_list)):
        min_i = i
        for j in range(i + 1, len(input_list)):
            if input_list[min_i] > input_list[j]: min_i = j
        input_list[i], input_list[min_i] = input_list[min_i], input_list[i]

    return (f"Сортировка выбором:       размер списка {len(input_list)} затраченное время {time.time() - start_time}")


array_size = [1000, 2000, 5000, 10000] # размеры массивов

for i in range(len(array_size)): # цикл вызовов сортировок

    random_array = [] # массив для рандомных чисел

    for r in range(array_size[i]): # заполнение массивов пустыми числами
        random_array.append(random.randrange(0, array_size[i]))

    random_array_copy = copy.copy(random_array)  #
    print(heap_sort(random_array_copy))

    random_array_copy = copy.copy(random_array)
    print(selection_sort(random_array_copy))

    random_array_copy = copy.copy(random_array)
    print(bubble_sort(random_array_copy), '\n')
