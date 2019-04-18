from difflib import SequenceMatcher

# dedupe a list
def unique(seq):  # Dave Kirby
    # Order preserving
    seen = set()
    return [x for x in seq if x not in seen and not seen.add(x)]


# compare similar strings
def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()


# fing packages with matching names in two different sets
def compare_packages(a, b):
    k = []
    for i in a:
        for j in b:
            if i == j.get("package"):
                k.append(j)
    return k
