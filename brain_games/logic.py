#!/usr/bin/env puthon3
def game_logic():
    import prompt
    name = prompt.string('May I have your name? ')
    print('Hello,', name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 1
    while i <= 3:
        import random
        digit = random.randint(1, 1000)
        print('Question:', digit)
        answer = prompt.string('Your answer: ')
        if answer == 'yes' and digit % 2 == 0:
            print('Correct!')
            if i == 3:
                print('Congratulations,', name + '!')
                break
            else:
                i += 1
        elif answer == 'no' and digit % 2 != 0:
            print('Correct!')
            if i == 3:
                print('Congratulations,', name + '!')
                break
            else:
                i += 1
        elif answer == 'yes' and digit % 2 != 0:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print("Let's try again,", name + '!')
            break
        elif answer == 'no' and digit % 2 == 0:
            print("'no' is wrong answer ;(. Correct answer was 'yes'.")
            print("Let's try again,", name + '!')
            break
        elif answer != 'yes' or answer != 'no':
            print("Please answer 'yes' or 'no'!")
            print("Let's try again,", name + '!')
            break
