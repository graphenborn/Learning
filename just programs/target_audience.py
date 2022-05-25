people = [
    {"sex": "m", "age": 12},
    {"sex": "w", "age": 12},
    {"sex": "m", "age": 15},
    {"sex": "m", "age": 20},
    {"sex": "m", "age": 13},
    {"sex": "m", "age": 27},
    {"sex": "w", "age": 31},
    {"sex": "m", "age": 17},
    {"sex": "w", "age": 17},
    {"sex": "m", "age": 12},
    {"sex": "m", "age": 42},
    {"sex": "w", "age": 25}
]
def male (x):
    return x["sex"] == "m"
    
def years (x):
    return x["age"] >= 20 and x["age"] <= 30

my_people = list(filter(years, filter(male, people)))
print (my_people)
