```
Create a function which checks a number for three different properties.
is the number prime?
is the number even?
is the number a multiple of 10?
Each should return either true or false, which should be given as an array. Remark: The Haskell variant uses data Property.
Examples
number_property(7)  # ==> [true,  false, false] 
number_property(10) # ==> [false, true,  true] 
The number will always be an integer, either positive or negative. Note that negative numbers cannot be primes, but they can be multiples of 10:
number_property(-7)  # ==> [false, false, false] 
number_property(-10) # ==> [false, true,  true] 
```

import math

def is_prime(number):
    
    if number < 2:
        return False
    
    if number == 2:
        return True
    
    if number % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True

def number_property(n: int) -> list:   
    return [is_prime(n), False if n%2 else True, n % 10 == 0]