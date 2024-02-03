import random
def BubbleSort(list):
    array = list.copy()
    flag = 1
    stop = len(array) - 1
    while flag == 1:
        flag = 0
        for i in range(stop):
            if array[i] > array[i + 1]:
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
                flag = 1
        stop -= 1
    return array


def SelectionSort(list):
    array = list.copy()
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    return array  


def RandomArray(len):
    array = random.sample(range(1, len+1), len)
    return array

def EmptyArray(len):
    array = [0] * len
    return array

def FillArray(array):
    for i in range(len(array)):
        n_input = int(input("Insert a number: "))
        array[i] = n_input

        

