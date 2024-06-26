```
Complete the function so that it takes a collection of keys and a default value and returns a hash (Ruby) / dictionary (Python) / map (Scala) with all keys set to the default value.

Example
populate_dict(["draft", "completed"], 0)  # should return {"draft": 0, "completed: 0}

```

def populate_dict(keys: list, default: int) -> dict:
    return dict.fromkeys(keys, default)