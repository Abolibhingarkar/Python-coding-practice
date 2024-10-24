import random
import time
correct_answer = random.randint(1,10)

print('Hi! Welcome to the number guessing game. I am going to pick a number between 1 and 10.')
time.sleep(3)
print('Picking a number...')
time.sleep(3)
guess_answer = int(input('What is your guess?: '))
guess_count = 1

while guess_answer != correct_answer:
    time.sleep(2)
    guess_count += 1
    if guess_answer > correct_answer:
        guess_answer = int(input('Your answer is greater than the correct answer. What is your guess?: '))
    else:
        guess_answer = int(input('Your answer is lower than the correct answer. What is your guess?: '))
    
time.sleep(2)
print(f'Congrats! You guessed the right answer and it took you {guess_count} guesses.')
