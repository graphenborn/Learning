students = [
    {"name": "Светлана", "avg_ball": 4.7},
    {"name": "София", "avg_ball": 5.0},
    {"name": "Егор", "avg_ball": 4.4},
    {"name": "Марина", "avg_ball": 4.2},
    {"name": "Дима", "avg_ball": 3.8},
    {"name": "Антон", "avg_ball": 4.0},
    {"name": "Милана", "avg_ball": 4.9},
    {"name": "Фёдор", "avg_ball": 4.5},
    {"name": "Татьяна", "avg_ball": 3.7}
]

gold = [x["name"] for x in students if x["avg_ball"] > 4.8]
silver = [x["name"] for x in students if x["avg_ball"] > 4.4 and x["avg_ball"]< 4.9]
print(gold)
print(silver)