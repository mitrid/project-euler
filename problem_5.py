number = 2520
result = None
while result is None:
    if all([True if number%i==0 else False for i in range(1, 21)]):
        result = number
    else:
        number+=2520
    print(number, end='\r')

print(f'Answer is: {result}')