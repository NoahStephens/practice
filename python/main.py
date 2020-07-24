import Queue

for num in range(0, 10000 + 1):
    if num > 1:
        for i  in range(2, num):
            if (num % i ) == 0:
                break
            else:
                queue.put(num)

print(queue.qsize)
