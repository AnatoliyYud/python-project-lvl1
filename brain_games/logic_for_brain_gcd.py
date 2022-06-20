#!/usr/bin/env puthon3


def game_gcd():
    import random
    import prompt
    import math
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print('Find the greatest common divisor of given numbers.')
    i = 1
    while i <= 3:
        first_digit = random.randint(1, 100)
        second_digit = random.randint(1, 100)
        correct_answer = math.gcd(first_digit, second_digit)
        print(f"Question: {first_digit} {second_digit}")
        answer = prompt.integer('Your answer: ',)
        if answer == correct_answer and i != 3:
            print('Correct!')
            i += 1
        elif answer == correct_answer and i == 3:
            print('Correct!')
            print(f"Congratulations, {name}!")
            break
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
