import random


def guessing_game():
    answer = random.randint(0,100)
    print(answer)
    attempt = 0
    while True:
        attempt += 1
        if attempt > 3:
            break
        guess = int(input("What is your guess? "))
        if guess > answer:
            print("Your {} too high".format(guess))
            print(f"You have only {3-attempt} attempts")
        elif guess < answer:
            print(f"Your {guess} too low")
            print(f"You have only {3-attempt} attempts")
        else:
            print(f"Yep, it took {attempt} attempts")
            break


guessing_game()
