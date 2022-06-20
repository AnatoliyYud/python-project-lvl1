#!/usr/bin/env puthon3


def game_calc():
    import random
    import prompt
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print('What is the result of the expression?')
    i = 1
    while i <= 3:
        first_digit = random.randint(0, 100)
        second_digit = random.randint(0, 100)
        action = random.choice(['+', '-', '*'])
        print(f"Question: {str(first_digit)} {action} {str(second_digit)}")
        answer = prompt.integer('Your answer: ',)
        if action == '+':
            correct_answer = first_digit + second_digit
            if answer == correct_answer and i != 3:
                print('Correct!')
                i += 1
            elif answer == correct_answer and i == 3:
                print('Correct!')
                print(f"Congratulations, {name}!")
                break
            else:
                print(f"'{str(answer)}' is wrong answer ;(. Correct answer was '{str(correct_answer)}'.")
                print(f"Let's try again, {name}!")
                break
        elif action == '-':
            correct_answer = first_digit - second_digit
            if answer == correct_answer and i != 3:
                print('Correct!')
                i += 1
            elif answer == correct_answer and i == 3:
                print('Correct!')
                print(f"Congratulations, {name}!")
                break
            else:
                print(f"'{str(answer)}' is wrong answer ;(. Correct answer was '{str(correct_answer)}'.")
                print(f"Let's try again, {name}!")
                break
        elif action == '*':
            correct_answer = first_digit * second_digit
            if answer == correct_answer and i != 3:
                print('Correct!')
                i += 1
            elif answer == correct_answer and i == 3:
                print('Correct!')
                print(f"Congratulations, {name}!")
                break
            else:
                print(f"'{str(answer)}' is wrong answer ;(. Correct answer was '{str(correct_answer)}'.")
                print(f"Let's try again, {name}!")
                break
