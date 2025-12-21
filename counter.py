from collections import Counter


def counter(s):
    freq = Counter(s)
    return freq

if __name__ == "__main__":
    print(counter("nivedhan"))