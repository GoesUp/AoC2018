day, star = input("Enter day: "), input("Enter star (1 or 2): ")
module = __import__("day" + day + ".day" + day, globals(), locals(), ["day" + day + "_" + star])
with open("input/day" + day + ".txt") as f:
    print(getattr(module, "day" + day + "_" + star)(f.read()))
