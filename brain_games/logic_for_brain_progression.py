#!/usr/bin/env puthon3


def game_progression():
    import random
    import prompt
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print('What number is missing in the progression?')
    i = 1
    while i <= 3:
        first_digit = random.randint(0, 50)
        step = random.randint(1, 50)
        result = [first_digit, ]
        digit = first_digit
        n = 1
        while n < 10:
            digit += step
            result.append(digit)
            n += 1
        correct_answer = random.choice(result)
        position = result.index(correct_answer)
        result[position] = '..'
        print('Question:', *result)
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
