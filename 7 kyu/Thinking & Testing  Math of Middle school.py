def mystery(al: list, bl: list) -> list:    
    a, b, c, d = al
    e, f, g, h = bl   
    return [a*e+b*g, a*f+b*h, c*e+d*g, c*f+d*h]