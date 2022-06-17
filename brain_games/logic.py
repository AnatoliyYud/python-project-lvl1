#!/usr/bin/env puthon3
def game_even():
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

def game_gcd():
    import random, prompt, math
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

def game_progression():
    import random, prompt, math
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print('What number is missing in the progression?')
    i = 1
    while i <= 3:
        first_digit = random.randint(0, 50)
        step = random.randint(1, 50)
        result = [first_digit,]
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
