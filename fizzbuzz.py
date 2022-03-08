def fizziness(div1, div2, n):

    FizzBuzz = ''
    for i in range(1, n+1, 1):
        if i % div1 == 0 and i % div2 != 0:
            print('Fizz')
            FizzBuzz += 'Fizz '
        elif i % div2 == 0 and i % div1 != 0:
            print('Buzz')
            FizzBuzz += 'Buzz '
        elif i % div1 == 0 and i % div2 == 0:
            print('FizzBuzz')
            FizzBuzz += 'FizzBuzz '
        else:
            print(i)
            FizzBuzz += (str(i) + ' ')

    return FizzBuzz


if __name__ == '__main__':

    fizziness(3, 5, 100)
