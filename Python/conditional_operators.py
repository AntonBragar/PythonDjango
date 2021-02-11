# user_input = int(input('How old are you? '))
#
# if user_input >= 18:
#     print("Welcome!")
# elif user_input < 18:
#     print("You`re too young")

# def checkAge():
#     name = input("What is your name? ")
#     user_input = int(input("How old are you? "))
#     if user_input >= 18:
#         print(f"Welcome {name}")
#     else:
#         print(f'You`re too young {name}')
#
# checkAge()


def answer():
    ans = input('Do you...? (yes/no): ')
    if ans.lower() == 'yes' or ans.lower() == 'y':
        print(f'Positive answer {ans}')
    elif ans.lower() == 'no' or ans.lower() == 'n':
        print(f'Negative answer {ans}')

answer()