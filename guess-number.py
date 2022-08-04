import random 
start = input('Please enter the smallest numebr:')
end = input('Please enter the largest numeber: ')
start = int(start)
end = int(end)

r = random.randint(start,end)
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