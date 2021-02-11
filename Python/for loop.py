# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# sum_of_numbers = 0
#
# for number in numbers:
#     sum_of_numbers += number
#     if number == 5 or number == 3:
#         break
# print(sum_of_numbers)


# tupple_list = [('a', 'b'), ('c', 'd'), ('e', 'f')]
#
# for item in tupple_list:
#     print(item)
#
# for letter_1, letter_2 in tupple_list:
#     print(letter_1, letter_2)

# tuple_list_1 = [('a', 'b', 5), ('c', 'd', 3), ('e', 'f', 7)]
# for letter_1, letter_2, number in tuple_list_1:
#     print(letter_1, letter_2, number)


dictionary = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3'
}
# for item in dictionary:
#     print(item)
# for item in dictionary.items():
#     print(item)
# for item in dictionary.keys():
#     print(item)
# for item in dictionary.values():
#     print(item)

for key, value in dictionary.items():
    print(key, value)