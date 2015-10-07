sumofsquares = 0
squareofsum = 0

for x in range(1,101):
    sumofsquares = sumofsquares + (x**2)
    squareofsum = squareofsum + x

squareofsum = squareofsum ** 2

print( squareofsum - sumofsquares)

#269147
