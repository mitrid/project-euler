import time
start_time = time.time()
number = 600851475143

i = 2
result = []
while i <= number:
    j = 1
    division_count = 0
    while j <= i and division_count < 3:
        if i%j == 0:
            division_count += 1
        j += 1
    if division_count == 2 and number % i == 0:
        number /= i
        result.append(i)
    if number % i != 0:
        i += 1  
print(f'Largest prime factor is: {max(result)}')
print(f'Finish at: {time.time()-start_time}')