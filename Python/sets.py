rainbow_colors = {'red', 'orange', 'yellow', 'green',
                  'blue', 'indigo', 'violet'}

print(rainbow_colors)
print(type(rainbow_colors))

empty_set = {}
print(empty_set)
print(type(empty_set))

number_list = [1, 43, 56]
text_tuple = ('hello', 'halo', 'sex')
set_from_list = set(number_list)
set_from_tuple = set(text_tuple)

print(set_from_list)
print(set_from_tuple)

set_from_list.add(5)
set_from_tuple.add('baby')

print(set_from_list)
print(set_from_tuple)

set_from_list.discard(5)
print(set_from_list)


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


dog = Animal('Jack', 5)
print(dog.name)

greetings = ['Hello', 'World']
print(greetings)
