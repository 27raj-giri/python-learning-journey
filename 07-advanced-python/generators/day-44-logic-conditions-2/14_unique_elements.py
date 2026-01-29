def unique(list):
    seen = set()
    for item in list:
        if item not in seen:
            seen.add(item)
            yield item

data = [10, 20, 10, 30, 20, 40, 50, 30]
for u in unique(data):
    print(u)