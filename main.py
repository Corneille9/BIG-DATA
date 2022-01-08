import string
from collections import defaultdict


def word_count(text):
    counts = defaultdict(int)
    for word in text.split():
        counts[word.lower()] += 1
    return counts


def map(key, value):
    intermediate = []
    for word in value.split():
        intermediate.append((word.lower(), 1))
    return intermediate


# fonction shuffle et sort
def sort_values(map_list):
    values = {}
    for map in map_list:
        for key, value in map:
            if values.get(key) is not None:  # verifier si cette clé existe déjà dans notre dictionnaire
                values.update({key: values.get(key) + [value]})
            else:
                values[key] = [value]
    return values


def reduce(key, values):
    result = 0
    for c in values:
        result = result + c
    return key, result


map_list = []
for filename in ["text1", "text2", "text3", "text4", "text5"]:
    with open(filename + ".txt", "r") as fic:
        map_list.append(map(filename, fic.read().translate(str.maketrans('', '', string.punctuation))))

sorted_values = sort_values(map_list)

for key, value in sorted_values.items():
    k, v = reduce(key, value)
    print(k, " ========>", v, " occurences")