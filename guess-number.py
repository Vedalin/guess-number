import random 
r = random.randint(1,100)
count = 0 
while True: 
    count = count + 1 
    num = input('Please guess the number: ')
    num = int(num)
    if num == r:
        print('You got it!')
        break
    elif num > r: 
        print('It is larger than the answer')
    elif num < r: 
        print('it is smaller than the answer')
    print('This is ', count, 'time you guess.')