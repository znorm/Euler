#largest prime factor

product = 0
big =0


for a in range(100, 999):
    for b in range(100, 999):
        product = a*b
        if str(a*b) == str(a*b)[::-1]:
            if product > big:
                big = product

print(big)
       
#254062
