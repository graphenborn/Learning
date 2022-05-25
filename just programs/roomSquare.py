from functools import reduce

rooms = [
    {"name": "кухня", "length": 6, "width": 4},
    {"name": "комната 1", "length": 5.5, "width": 4.5},
    {"name": "комната 2", "length": 5, "width": 4},
    {"name": "комната 3", "length": 7, "width": 6.3},
]

def roomSq(x):
    return x["length"] * x["width"]
    
def roomsSquare(x,y):
    return x+y
rooms = map(roomSq, rooms)
square = reduce(roomsSquare, rooms)
print(square)