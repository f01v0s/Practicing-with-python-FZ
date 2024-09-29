def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's have some fun.")
    print("Why do we use AI?")
    print("1. To make our tasks easier.")
    print("2. To learn and trust our sources.")
    print("3. To check our knowledge and try something different and new.")
    print("4. To keep up with the trend.")

    correct = 3  # This should not be indented inside the loop
    while True:
        answer = int(input())
        if answer == correct:
            print('Completed, have a nice day!')
            break  # Exit the loop once the correct answer is provided
        else:
            print("Please, try again.")


def end():
    print('Congratulations, have a nice day!')


# Call all the functions
greet('Aid', '2020')  # change as needed
remind_name()
guess_age()
count()
test()
end()
