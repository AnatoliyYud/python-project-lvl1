#!/usr/bin/env puthon3


def game_prime():
    import random
    import prompt
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 1
    while i <= 3:
        digit = random.randint(1, 50)
        print('Question:', digit)
        count = 0
        for n in range(1, digit // 2 + 1):
            if digit % n == 0:
                count += 1
        if count == 1:
            correct_answer = 'yes'
        if count != 1:
            correct_answer = 'no'
        answer = prompt.string('Your answer: ')
        if answer != 'yes' and answer != 'no':
            print("Please answer 'yes' or 'no'!")
            print("Let's try again,", name + '!')
            break
        else:
            if answer == correct_answer and i != 3:
                print('Correct!')
                i += 1
                continue
            elif answer == correct_answer and i == 3:
                print('Correct!')
                print(f"Congratulations, {name}!")
                break
            elif answer != correct_answer:
                print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
                print("Let's try again,", name + '!')
                break
