```
Oh no! Timmy's reduce is causing problems, Timmy's goal is to calculate the two teams scores and return the winner but timmy has gotten confused and sometimes teams don't enter their scores, total the scores out of 3! Help timmy fix his program!

Return true if team 1 wins or false if team 2 wins!



```

def calculate_total(t1, t2):
    t1_score = sum(score for score in t1 if score is not None)
    t2_score = sum(score for score in t2 if score is not None)
    
    return t1_score > t2_score