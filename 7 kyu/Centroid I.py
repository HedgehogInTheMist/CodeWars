def centroid(c):
    return [round(sum(x) / len(c), 2) for x in zip(*c)]