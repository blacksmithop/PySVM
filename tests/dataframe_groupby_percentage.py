from collections import Counter
import pandas as pd

data = [["A", 1], ["A", 2], ["B", 5], ["B", 5], ["B", 4], ["C", 6]]

df = pd.DataFrame(data, columns=["name", "id"])

id_all = df.groupby("name")["id"].agg(list)

id_unique = df.groupby("name")["id"].agg(set)


def roundToTwo(value, total):
    value = value / total
    value *= 100
    return round(value, 2)


def get_percentage(item: list) -> list:
    c = Counter(item)
    total = sum(c.values())
    percent = {key: roundToTwo(value, total) for key, value in c.items()}
    return percent


id_percentage = id_all.apply(lambda item: get_percentage(item))

print(id_percentage.head())
