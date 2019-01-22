sum_squares_nn = sum([i**2 for i in range(1, 101)])
square_of_sum = sum(range(1, 101))**2
print(f'Difference between the sum of the squares is {square_of_sum - sum_squares_nn}')