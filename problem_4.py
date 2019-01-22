import time
start = time.time()
max_product = 0

for i in reversed(range(100, 1000)):
    for j in reversed(range(100, 1000)):
        product = i*j
        if max_product < product:
            product_str = str(i*j)
            if product_str[:3] == product_str[-1:-4:-1]:
                max_product = product


print(f'Number: {max_product}')

# stolen version with generator
# from itertools import product
# result = max(
#     x*y for x, y in product(range(100, 999), range(100, 999)) 
#     if str(x*y) == "".join(reversed(str(x*y)))
# )

# stolen faster version 
# max_ = maxI = maxJ = 0
# i = 999
# j = 990
# while (i > 100):
#     j = 990
#     while (j > 100):
#         product = i * j
#         if (product > max_):
#             productString = str(product)
#             if (productString == productString[::-1]):
#                 max_ = product
#                 maxI = i
#                 maxJ = j
#         j -= 11
#     i -= 1
# print(max_, maxI, maxJ)
print(f'Finish at: {time.time()-start}')