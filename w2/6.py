import random
number = [i for i in range(random.randrange(1, 20))]
# print(number, len(number))
print('Number of even numbers: ', len(
    list(filter(lambda x: x % 2 == 0, number))))
print('Number of odd numbers: ', len(
    list(filter(lambda x: x % 2 == 1, number))))
