def total(*items):
    total = 0
    for (price, _) in items:
        total += price

    return total

print(total((10, "a"), (20, "b")))