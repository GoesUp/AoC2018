def star1(test: str) -> int:
    changes = test.split("\n")
    return sum(int(i) for i in changes)


def star2(test: str) -> int:
    changes = test.split("\n")
    frequency = 0
    previousStates = set()
    while True:
        for i in changes:
            frequency += int(i)
            if frequency in previousStates:
                return frequency
            previousStates.add(frequency)
