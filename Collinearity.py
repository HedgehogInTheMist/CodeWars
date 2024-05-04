```
You are given two vectors starting from the origin (x=0, y=0) with coordinates (x1,y1) and (x2,y2). Your task is to find out if these vectors are collinear. Collinear vectors are vectors that lie on the same straight line. They can be directed in the same or opposite directions. One vector can be obtained from another by multiplying it by a certain number. In terms of coordinates, vectors (x1, y1) and (x2, y2) are collinear if (x1, y1) = (k*x2, k*y2) , where k is any number acting as a coefficient.
Write the function collinearity(x1, y1, x2, y2), which returns a Boolean type depending on whether the vectors are collinear or not.

all coordinates are integers
-1000 <= any coordinate <= 1000
```
def collinearity(x1: int, y1: int, x2: int, y2: int) -> bool: 
    if x1 == y1 == 0 or x2 == y2 == 0:
        return True    
    return x1 * y2 == x2 * y1