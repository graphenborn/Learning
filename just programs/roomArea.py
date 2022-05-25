rooms = [
    {"name": "кухня", "length": 6, "width": 4},
    {"name": "комната 1", "length": 5.5, "width": 4.5},
    {"name": "комната 2", "length": 5, "width": 4},
    {"name": "комната 3", "length": 7, "width": 6.3},
]

def roomArea (x):
    x["square"] = x["length"] * x["width"]
    return x

rooms = list(map(roomArea, rooms))
print (rooms)