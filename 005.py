done = 'no'
x = 2520
good = 'y'
a=20
while done == 'no':
    x = x + 2520
    good = 'y'
    a=20

    
    
    while a > 10 and good != 'n':    
        print(x)
        print(a)
        
        good = 'y'
        if x % a == 0:
            good = 'y'
        else:
            good = 'n'
        a = a-1
            
    if good == 'y':
        done = 'yes'
    else:
        done = 'no'
        
print(x)


   
# to look up:
# douglas adams text adventure game
#267096th
