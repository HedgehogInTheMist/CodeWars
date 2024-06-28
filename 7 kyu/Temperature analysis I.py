```
You were given a string of integer temperature values. Create a function lowest_temp(t) and return
the lowest value or None/null/Nothing if the string is empty.
```

def lowest_temp(t):
  return min((int(x) for x in t.split()), default=None)
