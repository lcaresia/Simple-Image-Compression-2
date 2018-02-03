import time
import random

numbers = []
searchs = []
search_range = 1

for i in range(0, 9999):
    numbers.append((int(random.random() * 100), int(random.random() * 100), int(random.random() * 100)))
    searchs.append((int(random.random() * 100), int(random.random() * 100), int(random.random() * 100)))

start = time.time()
for search in searchs:
    for number in numbers:
        if (search[0] > (number[0] - search_range) and search[0] < (number[0] + search_range) and
            search[1] > (number[1] - search_range) and search[1] < (number[1] + search_range) and
            search[2] > (number[2] - search_range) and search[2] < (number[2] + search_range)):
            print(number)
            break

print('Time: %.2f' % (time.time() - start))