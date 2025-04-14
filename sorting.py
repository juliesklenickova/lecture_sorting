import csv
import os


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_name, mode='r', newline='', encoding='utf-8') as csvfile:
        data = {}
        reader = csv.DictReader(csvfile)
        for row in reader:
            for key, value in row.items():
                if key not in data:
                    data[key] = []
                # Převedeme hodnoty na čísla (int nebo float)
                try:
                    number = int(value)
                except ValueError:
                    number = float(value)
                data[key].append(number)
    return data
def selection_sort(numbers, direction='asc'):
    #slozitost on na druhou
    n = len(numbers)
    for i in range(n):
        index = i
        for j in range(i + 1, n):
            if direction == 'asc':
                if numbers[j] < numbers[index]:
                    index = j
            elif direction == 'desc':
                if numbers[j] > numbers[index]:
                    index = j
            else:
                raise ValueError("Parametr 'direction' musí být 'asc' nebo 'asc'.")
        numbers[i], numbers[index] = numbers[index], numbers[i]
    return numbers
def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers
def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key
    return numbers
def main():
    my_data = read_data("numbers.csv")
    print(my_data)
    print(selection_sort(my_data["series_1"]))
    print(bubble_sort(my_data["series_1"]))
    print(insertion_sort(my_data["series_3"]))
if __name__ == '__main__':
    main()
