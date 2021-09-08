from app import read_json

crds = read_json("./coords.json")
print(crds)

empty = read_json("./coords.")
print(empty)
