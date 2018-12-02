from collections import Counter


def is_different_by_one_letter(word1: str, word2: str) -> bool:  # Used in Star 2.
    if len(word1) == len(word2):
        diffs = 0
        for a, b in zip(word1, word2):
            if a != b:
                if diffs:
                    return False
                diffs += 1
        return True
    return False


def star1(test: str) -> int:
    data = test.splitlines()
    countTwos, countThrees = 0, 0
    for i in data:
        letterCount = Counter(i)
        if 3 in letterCount.values():
            countThrees += 1
        if 2 in letterCount.values():
            countTwos += 1
    return countTwos * countThrees


def star2(test: str) -> str:
    data = test.splitlines()
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if is_different_by_one_letter(data[i], data[j]):
                return "".join([data[i][w] for w in range(len(data[i])) if data[i][w] == data[j][w]])
