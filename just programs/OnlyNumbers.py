digits = ["12", "145", "  45", "12.4", "45,14", "15 645"]


def tofloat(x):
    return float(x.replace(",", ".").replace(" ", ""))
right_digits = list(map(tofloat, digits))

print (right_digits)