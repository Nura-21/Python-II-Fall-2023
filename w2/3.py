import random
guess = random.randint(1, 9)
# print(guess)
answer = int(input('Your guess: '))
while answer != guess:
    answer = int(input('Your guess again: '))
print('Well guessed!')
