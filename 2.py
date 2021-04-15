prevPrev = 1
acc = prev = 2
num = prevPrev + prev

while num < 4000000:
    if num % 2 == 0:
        acc += num
    num = prevPrev + prev
    prevPrev = prev
    prev = num

print(acc)
