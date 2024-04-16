print("------Задание 1------")
test_line_1 = input("Введите строку: ")
print("Обратная строка: ", test_line_1[::-1])

print("------Задание 2------")
test_line_2 = input("Введите строку: ")
result_line_2 = test_line_2[0]
for el in range(1, len(test_line_2)-1):
    if test_line_2[el] == 'h':
        result_line_2 += 'H'
    else:
        result_line_2 += test_line_2[el]
result_line_2 += test_line_2[-1]
print('Строка с измененной буквой H:',  result_line_2)

print("------Задание 3------")
test_line_3 = input("Введите строку: ")
print("Количество слов в строке: ", len(test_line_3.split()))

print("------Задание 4------")
test_line_4 = input("Введите строку: ")
num_words = 0
in_word = False

for el in test_line_4:
    if el.isalnum():
        if not in_word:
            num_words += 1
            in_word = True
    else:
        in_word = False
print("Количество слов в строке: ", num_words)

print("------Задание 5------")
test_line_5 = "Hello world"
new_line_5 = ' '.join(test_line_5.split()[::-1])
print('Строка с новым порядком слов:', new_line_5)

print("------Задание 6------")
name = input("Введите Ваше имя: ")
list_name = name.split()
result_name = list_name[0] + ' ' + list_name[1][0] + '. ' + list_name[2][0] + '.'
print(result_name)

print("------Задание 7------")
matryoshka_list = [33, [543.55, [1 + 8j, [[], 44, "Иголка"]]]]
print(matryoshka_list)

print("------Задание 8------")
test_list_8_1 = [3, 4, 22, 656, 33, 58, 3]
test_list_8_2 = ['b', 'o', 'n', 'j', 'o', 'u', 'r']
print(test_list_8_1 + test_list_8_2)
for el in test_list_8_2:
    test_list_8_1.append(el)
print(test_list_8_1)

print("------Задание 9------")
test_list_9_1 = [3, 4, 22, 656, 33, 58, 3]
test_list_9_2 = [5, 33, 13, 3232, 55, 33, 3]
test_list_9_3 = test_list_9_1 + test_list_9_2
no_repeats_list_9 = []
test_list_9_3 = sorted(test_list_9_3)
print("Отсортированный список:", test_list_9_3)
for el in test_list_9_3:
    if el not in no_repeats_list_9:
        no_repeats_list_9.append(el)
print("Список без повторений:", no_repeats_list_9)


print("------Задание 10------")
sequence_10 = [22, 33, 44, 66, 33]
check_set_10 = set(sequence_10)
print(sequence_10)
if len(check_set_10) == len(sequence_10):
    print("Числа последовательности уникальны")
else:
    print("Числа в последовательности не уникальны")

print("------Задание 11------")
date_dict = {'year': 2024, 'month': 4, 'day': 14}
print(date_dict['year'], '-', date_dict['month'], '-', date_dict['day'], sep='')

print("------Задание 12------")
test_line_12 = input("Введите числа, разделённые запятыми: ")
test_list_12 = list(map(int, test_line_12.split(',')))
test_set_12 = tuple(map(int, test_line_12.split(',')))
print("Список:", test_list_12)
print("Кортеж:", test_set_12)

print("------Задание 13------")
students = {'Schultz', 'Django', 'Brunhilde', 'Fritz'}
employees = {'Schultz', 'Django', 'Calvin', 'Butch', 'Fritz'}
print('Все люди:', students | employees)
print('Все люди:', students.union(employees))
print('И учатся, и работают:', students & employees)
print('И учатся, и работают:', students.intersection(employees))
print("Только работают, но не учатся", employees - students)
print("Только работают, но не учатся", employees.difference(students))
print("Либо учатся, либо работают, но не одновременно", students ^ employees)
print("Либо учатся, либо работают, но не одновременно", students.symmetric_difference(employees))


print("------Задание 14------")
array = [
    [11, 12, 13, 14, 15],
    [21, 22, 23, 24, 25],
    [31, 32, 33, 34, 35],
    [41, 42, 43, 44, 45],
    [51, 52, 53, 54, 55],
]

transposed_matrix = [[0 for j in range(len(array))] for i in range(len(array[0]))]
for i in range(len(array)):
    for j in range(len(array[i])):
        transposed_matrix[i][j] = array[j][i]
for i in range(len(array)):
    print(transposed_matrix[i])

print("------Задание 15------")
levels = int(input("Введите количество уровней пирамиды: "))
for i in range(0, levels):
    print('X', 'x'*i*2, 'X', sep='')
