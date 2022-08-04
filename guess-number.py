import random 
r = random.randint(1,100)
while True: 
    num = input('Please guess the number: ')
    num = int(num)
    if num == r:
        print('You got it!')
        break
    elif num > r: 
        print('It is larger than the answer')
    elif num < r: 
        print('it is smaller than the answer')