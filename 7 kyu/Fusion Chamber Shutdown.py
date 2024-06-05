```
A laboratory is testing how atoms react in ionic state during nuclear fusion. They introduce different elements with Hydrogen in high temperature and pressurized chamber. Due to unknown reason the chamber lost its power and the elements in it started precipitating
Given the number of atoms of Carbon [C],Hydrogen[H] and Oxygen[O] in the chamber. Calculate how many molecules of Water [H2O], Carbon Dioxide [CO2] and Methane [CH4] will be produced following the order of reaction affinity below
1. Hydrogen reacts with Oxygen   = H2O
2. Carbon   reacts with Oxygen   = CO2
3. Carbon   reacts with Hydrogen = CH4
FOR EXAMPLE:
(C,H,O) = (45,11,100)
return no. of water, carbon dioxide and methane molecules
Output should be like:
(5,45,0)
```
import math
# Make sure you follow the order of reaction
# output should be H2O,CO2,CH4
def burner(c: int, h: int, o: int) -> list:    
    H2O = h // 2 if (h // 2) < o else o if o < h else 0
    CO2 = c if c < (o - H2O) // 2 else (o - H2O) // 2 if c > (o - H2O) // 2 else 0
    CH4 = c - CO2 if c - CO2 < (h - 2 * H2O) // 4 else (h - 2 * H2O) // 4 if c - CO2 > (h - 2 * H2O) // 4 else 0    
    return (H2O, CO2, CH4)