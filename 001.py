import time
Sum = 0
for x in range(1,1000):
    if x % 3 ==0 or x % 5 ==0:
        Sum = Sum + x
        
print(Sum)

time.sleep(4)
# 471267th
