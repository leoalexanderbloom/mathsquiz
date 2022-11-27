import random

if __name__ == '__main__':
    print("\n\n=====================\nLeo's Cool Maths Game\n=====================\n")
    score = 0
    for x in range(1, 50):
        print("\nQuestion " + str(x) + " of 50: (current score: " + str(score) + ") \n")
        number_one = random.randrange(10, 75)
        number_two = random.randrange(1, 100)
        print("What is " + str(number_one) + " + " + str(number_two) + "?")
        try:
            user_input = input().strip()
            answer = int(user_input)
            if answer == number_one + number_two:
                print("Well done?")
                score = score + 100
            else:
                print("Sorry " + str(answer) + " is not correct, the answer is actually: " + str(number_one + number_two))
                score = score - 10
        except ValueError:
            print("Sorry \"" + user_input + "\" is not correct, the answer is actually: " + str(number_one + number_two))
    print("\nYour score was: " + str(score) + ") \n")
